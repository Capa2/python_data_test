# Big Data Module

A Python module for processing large datasets with swappable generator modules, and data transformation configurations. This module is currently configured to analyze playtime vs. review sentiment data from a large CSV file of game reviews.

Overview
    Modules:
        transform_data: Processes large CSV files in chunks, filtering and aggregating data.
        plots: Contains plotting functions, e.g., playtime_vs_sentiment, to visualize processed data.
        utils: Helper functions, including safe_open for safe file handling and logger for logging.

Setup
1. Clone the Repository

bash

git clone https://github.com/yourusername/big_data_module.git
cd big_data_module

2. Set Up a Virtual Environment

bash

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

3. Install Dependencies

bash

pip install -r requirements.txt

4. Ensure Data Directory

Place CSV data files in src/db/.
Running an Analysis
Configuration

Define configuration in config for processing and filtering data:

python

import os

config = {
    'source_data_path': os.path.join("src", "db", "reviews", "weighted_score_above_08.csv"),
    'aggregated_data_path': os.path.join("src", "db", "reviews", "processed_reviews.csv"),
    'chunk_size': 1000,
    'chunk_limit': None,
    'filter_cols': ['author_playtime_at_review', 'voted_up'],
    'delimiter': ";",
    'language': "english",
}

Run the Analysis

    Process Data: This will read and filter data from the CSV in chunks.

    python

from big_data.transform_data import process_data
process_data(config)

Generate Plot: Create a bar chart showing positive review percentages vs. playtime intervals.

python

    from big_data.plots.playtime_vs_sentiment import chart_data
    chart_data()

Example Output

    Chart: The generated bar chart visualizes positive review percentages across playtime intervals, providing insights into sentiment trends by engagement level.