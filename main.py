from src.analysis.analyzer import NetworkAnalyzer
from src.utils.generator import TrafficGenerator
import os

""" MAIN HELPER """
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def main(): 
    clear()
    filepath = "data/network_traffic.csv"

    """ Simulated data generator """
    gen = TrafficGenerator()
    gen.generate_csv(filepath, total_packets=100000)    # change 'total_packets' if you want another specific number.

    """ Analyzing & Visualization """
    detector = NetworkAnalyzer(filepath)
    detector.get_general_stats()
    detector.analyze_traffic()
    detector.plot_traffic()

if __name__ == "__main__":
    main()