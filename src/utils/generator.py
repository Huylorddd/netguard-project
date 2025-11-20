import random
import csv 
import os
import json

from src.core.protocol import TCP, UDP
from src.core.packet import Packet

class TrafficGenerator:
    def __init__(self, config_path="config.json"):
        self.config_path = config_path
        self.load_config()
    
    # config reader:: <- load IPs from ~/config.json file.
    def load_config(self):
        try:
            with open(self.config_path, 'r') as f:
                config = json.load(f)

                # Load IPs to class variables::
                self.target_ip = config.get("target_ip", "192.168.1.1")
                self.normal_ip = config.get("normal_ip", [])
                self.ddos_ip   = config.get("ddos_ip", [])

                print(f"Loaded {len(self.normal_ip)} normal IPs and {len(self.ddos_ip)} DDoS IPs.")

        except FileNotFoundError:
            print(f"FileNotFound: Cannot find the config file at {self.config_path}.")
            # Using hardcoded data (default) to avoid crashing::
            self.target_ip = "192.168.1.1"
            self.normal_ip = ["192.168.1.15"]
            self.ddos_ip   = ["6.6.6.6"]

    def generate_single_packet(self, is_attack=False):
        if is_attack:
            src_ip = random.choice(self.ddos_ip)
            psize = random.randint(10, 50)
            port = 80
        else:
            src_ip = random.choice(self.normal_ip)
            psize = random.randint(100, 1500)
            port = random.randint(1024, 65535) # Above 1024 is safe and avoiding system runs.
        
        dest_ip = self.target_ip
        protocol_class = random.choice([TCP, UDP])    # Source protocol can be both.
        protocol = protocol_class(port=port)
        return Packet(src_ip, dest_ip, protocol, psize)
    

    def generate_csv(self, filename, total_packets):
        print(f"Creating {total_packets} packets into {filename}...")

        with open(filename, "w", newline='') as f:
            # Using csv library::
            writer = csv.writer(f)

            # Header::
            writer.writerow(["Timestamp", "Source_IP", "Dest_IP", "Protocol", "Port", "Size"])

            for i in range(total_packets):
                if random.random() < 0.1:
                    packet = self.generate_single_packet(is_attack=True)
                else:
                    packet = self.generate_single_packet(is_attack=False)

                proto_name = "TCP" if isinstance(packet.protocol, TCP) else "UDP"

                row = [
                    packet.timestamp,
                    packet.source_ip,
                    packet.dest_ip,
                    proto_name,
                    packet.protocol.port,
                    packet.payload_size
                ]
                writer.writerow(row)

        print("Generated sucessfully !")
