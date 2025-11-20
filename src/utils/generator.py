import random
import csv 

from src.core.protocol import TCP, UDP
from src.core.packet import Packet

class TrafficGenerator:
    def __init__(self):
        self.target_ip = "192.168.1.1"
        self.normal_ip = ["192.168.1.10", "192.168.1.11", "192.168.1.12"]
        self.ddos_ip   = ["80.82.77.139", "2.57.121.112", "183.81.33.184"]
        

    def generate_single_packet(self, is_attack=False):
        if is_attack:
            src_ip = random.choice(self.ddos_ip)
            psize = random.randint(10, 50)
        else:
            src_ip = random.choice(self.normal_ip)
            psize = random.randint(1000, 9000)
        
        dest_ip = self.target_ip
        protocol_class = random.choice([TCP, UDP])    # Source protocol can be both.
        protocol = protocol_class(port=80)
        return Packet(src_ip, dest_ip, protocol, psize)
    

    def generate_csv(self, filename, total_packets):
        with open(filename, "w") as f:
            f.write("Timestamp,Source_IP,Dest_IP,Protocol,Port,Size\n")   # csv header
            for i in range(total_packets):
                if random.randint(1,10) > 9:    # 90/10 ratio for packets generator.
                    data = self.generate_single_packet(is_attack=True)
                else:
                    data = self.generate_single_packet(is_attack=False)
                f.write(f"{data.timestamp},{data.source_ip},{data.dest_ip},{data.protocol},{data.protocol.port},{data.payload_size}\n")
