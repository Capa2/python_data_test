import os
from big_data.analysis import playtime_vs_sentiment
import matplotlib.pyplot as plt

def main():
    playtime_vs_sentiment.prep_data()
    playtime_vs_sentiment.chart_data()
    plt.show()
