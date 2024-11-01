#big_data/analysis/language_dist_in_reviews.py
# big_data/analysis/language_dist_in_reviews.py

import os
import pandas as pd
from big_data.utils.data_writer import write_chunks_to_preprocessed_file
from big_data.utils.csv_reader import read_csv_in_chunks
from big_data.utils.chunk_processor import chunk_processor
from utils.plot_helper import pie_chart
from utils.log_helper import get_logger

LOGGER = get_logger("language_dist_in_reviews")

config = {
    'source_data_path': os.path.join("src", "db", "reviews", "extracts", "some_reviews.csv"),
    'preprocessed_data_path': os.path.join("src", "db", "reviews", "preprocessed", "language_distribution.csv"),
    'delimiter': ";",
    'chunk_size': 2000,
    'chunk_limit': None,
    'chunk_row_limit': None,
    'filter_cols': ['language'],
    'lang_filter': None
}

def aggregate_language_distribution(chunk):
    return chunk['language'].value_counts().sort_values(ascending=False)

def combine_language_aggregates(results):
    combined = pd.concat(results, axis=1).fillna(0).sum(axis=1)
    return combined

def preprocess_data_to_file():
    write_chunks_to_preprocessed_file(config)

def compute_aggregated_metrics():
    aggregated_data = chunk_processor(
        generator=read_csv_in_chunks(config),
        process_func=aggregate_language_distribution,
        aggregate_func=combine_language_aggregates,
        config=config
    )

    if aggregated_data is not None:
        total_count = aggregated_data.sum()

        labels = []
        sizes = []
        other_size = 0

        for label, size in zip(aggregated_data.index, aggregated_data.values):
            percentage = (size / total_count) * 100
            if percentage >= 2:
                labels.append(label)
                sizes.append(size)
            else:
                other_size += size

        if other_size > 0:
            labels.append("Other")
            sizes.append(other_size)

        return labels, sizes
    else:
        LOGGER.error("No data to process.")
        return [], []


def chart_data():
    labels, sizes = compute_aggregated_metrics()
    pie_chart(
        labels=labels,
        sizes=sizes,
        title="Language Distribution in Reviews",
        labeldistance=1.025,
        textprops={'fontsize': 8}
    )
