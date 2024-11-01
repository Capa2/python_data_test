# big_data/analysis/analysis_template.py

import os
from big_data.utils import data_writer
from utils.plot_helper import bar_chart
from utils.safe_open import safe_open

config = {
    'source_data_path': os.path.join("src", "db", "reviews", "all_reviews", "all_reviews.csv"),
    'preprocessed_data_path': os.path.join("src", "db", "reviews", "extracts", "some_reviews.csv"),
    'delimiter': ";",
    'chunk_size': 2000,
    'chunk_limit': 10000,
    'chunk_row_limit': 2,
    'filter_cols': None,
    'lang_filter': None,
}

def prepare_data_chunks():
    data_writer.write_chunks_to_preprocessed_file(config)