# big_data/analysis/analysis_template.py

import os
from big_data.utils import aggregate_chunked_data
from utils.plot_helper import bar_chart
from utils.safe_open import safe_open

config = {
    'source_data_path': os.path.join("src", "db", "reviews", "all_reviews", "all_reviews.csv"),
    'aggregated_data_path': os.path.join("src", "db", "reviews", "extracts", "some_reviews.csv"),
    'delimiter': ";",
    'chunk_size': 2000,
    'chunk_limit': 10000,
    'chunk_row_limit': 2,
    'filter_cols': None,
    'lang_filter': None,
}

def prepare_data_chunks():
    aggregate_chunked_data.aggregate_from_source(config)