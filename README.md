# Big Data Analysis Module

This module is designed for processing large datasets in chunks, filtering them, and generating custom analyses such as playtime vs. sentiment analysis. Key utilities support chunk-based processing and configurable data transformations.

## Overview of Main Components

### src/big_data/

- main.py: Runs an analysis analysis and displays plot

- utils/**chunk_processor.py:** Processes and optionally aggregates data in chunks from a generator.
    - chunk_processor(): Main entry point, applying a function to each chunk and optionally supply an aggrigator.
    - is_chunk_limit_reached() / filter_chunk_data(): Configurable checks for data limits and filtering.

- utils/**data_writer.py**: Handles chunked data preprocessing and file writing based on configuration.
    - write_chunks_to_preprocessed_file(): Processes CSV in chunks and writes to a file.
    - transform_and_append_chunk(): Transforms and appends each chunk to the preprocessed file.

- utils/**csv_reader.py**: Reads CSVs in chunks.
    - read_csv_in_chunks(): Yields CSV chunks based on config settings.
 
### src/big_data/analysis

- Contains specific analysis

### src/utils/

- Logging (utils/log_helper.py): Logs processes and errors to a file and console for debugging.
- plotting (utils/plot_helper.py): Creates visualizations like bar charts, histograms, etc.
- safe_open (utils/safe_open.py): Safely opens files with error handling for common file issues.

## Data set
- Full dataset:
    - https://www.kaggle.com/datasets/kieranpoc/steam-reviews

Partial dataset:
    - a partial dataset has been extracted at: /src/db/reviews/extracts/some_reviews.csv

## Creating a New Analysis

- Duplicate the analysis_template.py and update config.
- Define compute_aggregated_metrics() and chart_data() for your analysis.

Each analysis file will only need to configure settings and define analysis logic and/or visualisation.
