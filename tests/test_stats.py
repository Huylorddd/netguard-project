from src.analysis.analyzer import NetworkAnalyzer

def main():
    filepath = "data/network_traffic.csv"

    test = NetworkAnalyzer(filepath)
    test.get_general_stats()
    test.analyze_traffic()
    test.plot_traffic()

if __name__ == "__main__":
    main()