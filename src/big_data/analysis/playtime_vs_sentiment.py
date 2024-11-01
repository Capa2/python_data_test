# big_data/analysis/playtime_vs_sentiment.py

import os
import pandas as pd
from big_data.utils import aggregate_chunked_data
from utils.plot_helper import bar_chart
from utils.safe_open import safe_open

config = {
    'source_data_path': os.path.join("src", "db", "reviews", "all_reviews", "all_reviews.csv"),
    'aggregated_data_path': os.path.join("src", "db", "reviews", "analysis", "sentiment_playtime.csv"),
    'delimiter': ";",
    'chunk_size': 2000,
    'chunk_limit': None,
    'chunk_row_limit': None,
    'filter_cols': ['author_playtime_at_review', 'voted_up'],
    'lang_filter': None, # Filter by language or None for all languages
}

def prepare_data_chunks():
    aggregate_chunked_data.aggregate_from_source(config)

def compute_aggregated_metrics():
    with safe_open(config['aggregated_data_path']) as file:
        df = pd.read_csv(file, delimiter=config['delimiter'])

        bins = [0, 3, 11, 21, 51, 101, 201, 501, float("inf")]
        labels = ["0-2", "3-10", "11-20", "21-50", "51-100", "101-200", "201-500", "500+"]

        df['playtime_bin'] = pd.cut(df['author_playtime_at_review'], bins=bins, labels=labels, right=False)

        sentiment_counts = df.groupby(['playtime_bin', 'voted_up']).size().unstack(fill_value=0)
        sentiment_counts['total'] = sentiment_counts[0] + sentiment_counts[1]
        sentiment_counts['positive_percentage'] = (sentiment_counts[1] / sentiment_counts['total']) * 100
        
        x_data = sentiment_counts.index.astype(str).tolist()
        y_data = sentiment_counts['positive_percentage'].tolist()
        return x_data, y_data

def chart_data():
    x_data, y_data = compute_aggregated_metrics()
    bar_chart(
        x_data=x_data,
        y_data=y_data,
        x_label="Playtime Intervals (hours)",
        y_label="Percentage of Positive Reviews (%)",
        title="Percentage of Positive Reviews vs. Playtime",
        rotate_labels=False
    )