import datetime

# Run from main.py::
from src.core.protocol import Protocol

class Packet:
    def __init__(self, source_ip, dest_ip, protocol : Protocol, payload_size):
        self.source_ip = source_ip
        self.dest_ip = dest_ip
        self.protocol = protocol
        self.payload_size = payload_size
        self.timestamp = datetime.datetime.now()

    def display_info(self):
        return f"[{self.timestamp}] {self.source_ip} -> {self.dest_ip} | {self.protocol}:{self.protocol.port} | {self.payload_size}\n"