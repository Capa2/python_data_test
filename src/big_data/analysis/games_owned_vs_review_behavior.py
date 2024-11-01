import os
import pandas as pd
from big_data.utils.chunk_processor import chunk_processor
from big_data.utils.csv_reader import read_csv_in_chunks
from utils.plot_helper import bar_chart
from utils.log_helper import get_logger

LOGGER = get_logger("games_owned_reviews")

config = {
    'source_data_path': os.path.join("src", "db", "reviews", "extracts", "some_reviews.csv"),
    'preprocessed_data_path': os.path.join("src", "db", "reviews", "preprocessed", "games_owned_reviews.csv"),
    'delimiter': ";",
    'chunk_size': 2000,
    'chunk_limit': None,
    'chunk_row_limit': None,
    'filter_cols': ['author_num_games_owned', 'voted_up'],
    'lang_filter': None,
}

bins = [0, 4, 11, 21, 51, 101, 201, float("inf")]
labels = ["0-3", "4-10", "11-20", "21-50", "51-100", "101-200", "200+"]

def aggregate_reviews(chunk, config=None):
    chunk['games_owned_bin'] = pd.cut(chunk['author_num_games_owned'], bins=bins, labels=labels, right=False)
    return chunk.groupby('games_owned_bin', observed=True)['voted_up'].value_counts().unstack(fill_value=0)

def combine_reviews(results, config=None):
    combined = pd.concat(results)
    final_result = combined.groupby(combined.index, observed=True).sum()
    final_result['positive_percentage'] = (final_result[1] / (final_result[0] + final_result[1])) * 100
    return final_result

def compute_aggregated_metrics():
    aggregated_data = chunk_processor(
        generator=read_csv_in_chunks(config), 
        process_func=aggregate_reviews, 
        aggregate_func=combine_reviews,
        config=config
    )

    if aggregated_data is not None:
        x_data = aggregated_data.index.astype(str).tolist()
        y_data = aggregated_data['positive_percentage'].tolist()
        return x_data, y_data
    else:
        LOGGER.error("No data to process.")
        return [], []

def chart_data():
    x_data, y_data = compute_aggregated_metrics()
    bar_chart(
        x_data=x_data,
        y_data=y_data,
        x_label="Games Owned (binned)",
        y_label="Percentage of Positive Reviews (%)",
        title="Review Sentiment Distribution by Games Owned",
        rotate_labels=True
    )
