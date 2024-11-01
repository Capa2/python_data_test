import os
import pandas as pd
from big_data.utils import aggregate_chunked_data
from utils.plot_helper import boxplot
from utils.safe_open import safe_open

config = {
    'source_data_path': os.path.join("src", "db", "reviews", "all_reviews", "all_reviews.csv"),
    'aggregated_data_path': os.path.join("src", "db", "reviews", "aggregate", "games_owned_reviews.csv"),
    'delimiter': ";",
    'chunk_size': 2000,
    'chunk_limit': None,
    'chunk_row_limit': None,
    'filter_cols': ['author_num_games_owned', 'voted_up'],
    'lang_filter': None,
}

def prepare_data_chunks():
    aggregate_chunked_data.aggregate_from_source(config)

def compute_aggregated_metrics():
    with safe_open(config['aggregated_data_path']) as file:
        df = pd.read_csv(file, delimiter=config['delimiter'])

        # Define bins for the number of games owned
        bins = [0, 4, 11, 21, 51, 101, 201, float("inf")]
        labels = ["0-3", "4-10", "11-20", "21-50", "51-100", "101-200", "200+"]

        # Bin the 'author_num_games_owned' column
        df['games_owned_bin'] = pd.cut(df['author_num_games_owned'], bins=bins, labels=labels, right=False)

        # Prepare data as a DataFrame with bins and corresponding sentiment values
        plot_data = df[['games_owned_bin', 'voted_up']].dropna()

        return plot_data

def chart_data():
    boxplot(
        data=compute_aggregated_metrics(),
        x_label="Games Owned (binned)",
        y_label="Review Sentiment (1=Positive, 0=Negative)",
        title="Review Sentiment Distribution by Games Owned",
        rotate_labels=True
    )
