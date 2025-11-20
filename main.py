from src.core.protocol import TCP, UDP
from src.core.packet import Packet


http = TCP(port=80)
pkt = Packet("192.168.1.5", "8.8.8.8", http, 500)

print(pkt.display_info())