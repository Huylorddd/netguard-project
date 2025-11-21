from src.analysis.analyzer import NetworkAnalyzer
import os

def main():
    filepath = "data/network_traffic.csv"

    gen = TrafficGenerator()
    gen.generate_csv(filepath, total_packets=100000)    # change 'total_packets' if you want another specific number.


if __name__ == "__main__":
    main()