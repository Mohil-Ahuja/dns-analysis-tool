# dns_visualizer.py
import matplotlib.pyplot as plt

def plot_top_queries(query_counts):
    labels, values = zip(*query_counts.most_common(10))
    plt.bar(labels, values)
    plt.title("Top 10 DNS Queries")
    plt.xlabel("Domain Names")
    plt.ylabel("Number of Queries")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
