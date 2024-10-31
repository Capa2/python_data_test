# Big Data Analysis Module

This module is designed for processing large datasets in chunks, filtering them, and generating custom analyses such as playtime vs. sentiment analysis. Key utilities support chunk-based processing and configurable data transformations.

## Overview of Main Components

    - big_data/analysis/playtime_vs_sentiment.py: Contains the analysis logic for playtime vs. sentiment.
        - prepare_data_chunks(): Processes the raw CSV in chunks.
        - compute_aggregated_metrics(): Aggregates and bins data for playtime intervals and sentiment.
        - chart_data(): Generates a bar chart to visualize sentiment percentages by playtime interval.

    - big_data/utils/csv_chunk_processor.py: Generic chunk processor.
        - process_csv(): Main entry point for chunked processing, calling a specified function on each chunk.
        - write_chunk_to_file(): Writes processed chunks to the output file.
        - transform_headers() / transform_rows(): Customizable functions for data filtering or transformation.

    - big_data/utils/apply_to_chunked_data_from_generator.py: Supports chunk processing.
        - apply_to_chunked_data_from_generator(): Applies a given function to each chunk in the generator.

    - big_data/csv_generator.py: Generator for reading large CSVs in chunks.
        - csv_chunk_generator(): Yields chunks from a CSV based on config settings.

    - Logging (utils/log_helper.py): Logs processes and errors to a file and console for debugging.

## Usage

### Running the Playtime vs. Sentiment Analysis

The main entry point is src/main.py, which runs big_data/main.py, which initializes the playtime vs. sentiment analysis. To run the analysis:

- Set up configuration in playtime_vs_sentiment.py.
    - Run:

        python

        import os
        from big_data.analysis import playtime_vs_sentiment
        import matplotlib.pyplot as plt

        def main():
            playtime_vs_sentiment.prepare_data_chunks()
            playtime_vs_sentiment.chart_data()
            plt.show()

### Creating a New Analysis

- Duplicate the analysis_template.py and update config.
- Define compute_aggregated_metrics() and chart_data() for your analysis.

Each analysis file will only need to configure chunk settings and define the specific computation logic for metrics or charts.
