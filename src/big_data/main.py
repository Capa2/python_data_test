# big_data/main.py

import os
from big_data.analysis import playtime_vs_sentiment, extract_sample, games_owned_vs_review_behavior
import matplotlib.pyplot as plt

def main():

    analysis = games_owned_vs_review_behavior

    analysis.prepare_data_chunks()
    analysis.chart_data()

    plt.show()