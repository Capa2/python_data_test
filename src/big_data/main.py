# big_data/main.py

import os
from big_data.analysis import playtime_vs_sentiment, extract_sample
import matplotlib.pyplot as plt

def main():
    
    extract_sample.prepare_data_chunks()
    # playtime_vs_sentiment()

def playtime_vs_sentiment():
    playtime_vs_sentiment.prepare_data_chunks()
    playtime_vs_sentiment.chart_data()
    plt.show()