#big_data/playtime_vs_sentiment.py

import os
import pandas as pd
from big_data.utils.data_writer import write_chunks_to_preprocessed_file
from big_data.utils.csv_reader import read_csv_in_chunks
from big_data.utils.chunk_processor import chunk_processor
from utils.plot_helper import bar_chart
from utils.log_helper import get_logger

LOGGER = get_logger("playtime_vs_sentiment")

config = {
    'source_data_path': os.path.join("src", "db", "reviews", "extracts", "some_reviews.csv"),
    'preprocessed_data_path': os.path.join("src", "db", "reviews", "preprocessed", "some_sentiment_playtime.csv"),
    'delimiter': ";",
    'chunk_size': 2000,
    'chunk_limit': None,
    'chunk_row_limit': None,
    'filter_cols': ['author_playtime_at_review', 'voted_up'],
    'lang_filter': None
}

bins = [0, 3, 11, 21, 51, 101, 201, 501, float("inf")]
labels = ["0-2", "3-10", "11-20", "21-50", "51-100", "101-200", "201-500", "500+"]

def aggregate_playtime_sentiment(chunk):
    chunk['playtime_bin'] = pd.cut(chunk['author_playtime_at_review'], bins=bins, labels=labels, right=False)
    return chunk.groupby(['playtime_bin', 'voted_up'], observed=True).size().unstack(fill_value=0)

def combine_sentiment_aggregates(results):
    combined = pd.concat(results)
    final_result = combined.groupby(combined.index, observed=True).sum()
    final_result['total'] = final_result[0] + final_result[1]
    final_result['positive_percentage'] = (final_result[1] / final_result['total']) * 100
    return final_result

def preprocess_data_to_file():
    write_chunks_to_preprocessed_file(config)

def compute_aggregated_metrics():
    aggregated_data = chunk_processor(
        generator=read_csv_in_chunks(config),
        process_func=aggregate_playtime_sentiment,
        aggregate_func=combine_sentiment_aggregates,
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
        x_label="Playtime Intervals (hours)",
        y_label="Percentage of Positive Reviews (%)",
        title="Percentage of Positive Reviews vs. Playtime",
        rotate_labels=False
    )
