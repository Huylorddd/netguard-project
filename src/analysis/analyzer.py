import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class NetworkAnalyzer:
    def __init__(self, filepath):
        self.filepath = filepath
        self.load_data()

    def load_data(self):
        try:
            print(f"Loading data from {self.filepath}")
            self.df = pd.read_csv(self.filepath)
            print("Data loaded successfully.")

        except FileNotFoundError:
            print(f"FileNotFound: {self.filepath} does not exist.")
            self.df = None  # Default to avoid crashing.

    def get_general_stats(self):
        if self.df is None:
            print("No data to analyze.")
            return
        
        print("\n - -=< GENERAL STATISTICS >=- -")
        print(f"Total packets: {self.df.shape[0]}")     # Header is not counted.
        print(f"Unique IPs: {self.df['Source_IP'].nunique()}")
        print(f"Total size: {self.df['Size'].sum()}")
        print(self.df.head(5))

    
    """ ANOMALY DETECTOR """
    def analyze_traffic(self):
        if self.df is None:
            return
        
        print("\n - -=< TRAFFIC ANALYSIS REPORT >=- -")
        
        # Grouping & Aggregation::
        packet_counts = self.df.groupby('Source_IP')['Source_IP'].count()
        bytes_sent = self.df.groupby('Source_IP')['Size'].sum()

        # Summary::
        stats = pd.concat([packet_counts, bytes_sent], axis=1)
        stats.columns = ['Packet_Count', 'Total_Bytes'] # Renaming

        # Top 5 IPs have most sent::
        print("\n--- Top 5 IPs sending most packets ---")
        print(stats.sort_values(by='Packet_Count', ascending=False).head(5))
        
        # Anomaly detecting::
        threshold = 1000    # a specific number of packets that an IP could send. If over this, might be the DDoS attack.
        print(f"\n--- Suspicious IPs has been detected (Over {threshold} packets) ---")
        suspicious_ip = stats[stats['Packet_Count'] > threshold]

        if len(suspicious_ip) > 0:
            print("Alert: Found potential DDoS attacker.")
            print(suspicious_ip)
        else:
            print("No anomalies detected. Network is safe.")


    """ DATA VISUALIZATION """
    def plot_traffic(self):
        if self.df is None:
            return
        
        print("Plotting data...")
        
        # Data collecting::
        packet_counts = self.df.groupby('Source_IP')['Source_IP'].count()

        # Visualizing::
        plt.figure(figsize=(15,5))
        plt.bar(packet_counts.index, packet_counts.values, color='skyblue')

        ## Decorating
        plt.xlabel('Source IP')
        plt.ylabel('Packet Count')
        plt.title('Network Traffic Analysis: Packet Count per IP')
        plt.xticks(rotation=45)     # For IPs readable

        ## Threshold and its mentioning:
        plt.axhline(y=1000, color='r', linestyle='--', label='DDoS Threshold (1000)')
        plt.legend() 
        
        print("Displaying graph...")
        plt.tight_layout() 
        plt.show() 