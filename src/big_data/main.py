# big_data/main.py

import os
from big_data.analysis import extract_sample, playtime_vs_sentiment, language_dist_in_reviews, games_owned_vs_review_behavior
import matplotlib.pyplot as plt

def main():

    analysis = language_dist_in_reviews

    analysis.preprocess_data_to_file()
    analysis.chart_data()

    plt.show()