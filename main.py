from src.utils.generator import TrafficGenerator
import os

def main():
    if not os.path.exists("data"):
        os.mkdir("data")
    
    # Data generator::
    gen = TrafficGenerator()
    gen.generate_csv("data/network_traffic.csv", total_packets=30000)

if __name__ == "__main__":
    main()