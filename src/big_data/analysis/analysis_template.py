# big_data/analysis/analysis_template.py

import os
import pandas as pd
from big_data.utils import csv_chunk_processor
from utils.plots import bar_chart
from utils.safe_open import safe_open

config = {
    'source_data_path': os.path.join("src", "db", "reviews", "all_reviews", "all_reviews.csv"),
    'aggregated_data_path': os.path.join("src", "db", "reviews", "extracts", "template_analysis.csv"),
    'chunk_size': 2000,
    'chunk_limit': None,
    'row_per_chunk': None,
    'filter_cols': ['author_playtime_at_review', 'voted_up'],
    'delimiter': ";",
    'lang_filter': None,
}

def prepare_data_chunks():
    csv_chunk_processor.process_csv(config)

def compute_aggregated_metrics():
    with safe_open(config['aggregated_data_path']) as file:
        df = pd.read_csv(file, delimiter=config['delimiter'])

        x_data = y_data = []

        return x_data, y_data

def chart_data():
    x_data, y_data = compute_aggregated_metrics()
    bar_chart(
        x_data=x_data,
        y_data=y_data,
        x_label="x label",
        y_label="y label",
        title="title",
        rotate_labels=False
    )