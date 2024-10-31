import os
from big_data.analysis import playtime_vs_sentiment
import matplotlib.pyplot as plt

def main():
    #playtime_vs_sentiment.prepare_data_chunks()
    playtime_vs_sentiment.chart_data()
    plt.show()
