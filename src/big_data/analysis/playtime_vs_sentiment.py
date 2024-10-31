import os
import pandas as pd
from big_data.transform_data import process_data
from utils.plots import bar_chart
from utils.safe_open import safe_open

config = {
    'read_path': os.path.join("src", "db", "reviews", "all_reviews", "all_reviews.csv"),
    'write_path': os.path.join("src", "db", "reviews", "sentiment_playtime.csv"),
    'chunk_size': 2000,
    'chunk_limit': None,
    'row_per_chunk': None,
    'filter_cols': ['author_playtime_at_review', 'voted_up'],
    'delimiter': ";",
    'language_filter': None, # Filter by language or None for all languages
}

def prep_data():
    process_data(config)

def collect_data():
    with safe_open(config['write_path']) as file:
        df = pd.read_csv(file, delimiter=config['delimiter'])

        bins = [0, 3, 11, 21, 51, 101, 201, 501, float("inf")]
        labels = ["0-2", "3-10", "11-20", "21-50", "51-100", "101-200", "201-500", "500+"]

        df['playtime_bin'] = pd.cut(df['author_playtime_at_review'], bins=bins, labels=labels, right=False)

        sentiment_counts = df.groupby(['playtime_bin', 'voted_up']).size().unstack(fill_value=0)
        sentiment_counts['total'] = sentiment_counts[0] + sentiment_counts[1]
        sentiment_counts['positive_percentage'] = (sentiment_counts[1] / sentiment_counts['total']) * 100
        
        x_data = sentiment_counts.index.astype(str).tolist()  # Convert intervals to string labels
        y_data = sentiment_counts['positive_percentage'].tolist()
        return x_data, y_data

def chart_data():
    x_data, y_data = collect_data()
    bar_chart(
        x_data=x_data,
        y_data=y_data,
        x_label="Playtime Intervals (hours)",
        y_label="Percentage of Positive Reviews (%)",
        title="Percentage of Positive Reviews vs. Playtime",
        rotate_labels=False
    )