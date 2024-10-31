# Big Data Analysis Module

This module is designed for processing large datasets in chunks, filtering them, and generating custom analyses such as playtime vs. sentiment analysis. Key utilities support chunk-based processing and configurable data transformations.

## Overview of Main Components

### src/big_data/

- main.py: Runs playtime_vs_sentiment analysis in full and displays plot

- analysis/**playtime_vs_sentiment.py:** Contains the analysis logic for playtime vs. sentiment.
    - prepare_data_chunks(): Processes the raw CSV in chunks.
    - compute_aggregated_metrics(): Aggregates and bins data for playtime intervals and sentiment.
    - chart_data(): Generates a bar chart to visualize sentiment percentages by playtime interval.

- utils/**csv_chunk_processor.py:** Generic chunk processor.
    - process_csv(): Main entry point for chunked processing, calling a specified function on each chunk.
    - write_chunk_to_file(): Writes processed chunks to the output file.
    - transform_headers() / transform_rows(): Customizable functions for data filtering or transformation.

- utils/**apply_to_chunked_data_from_generator.py**: Supports chunk processing.
    - apply_to_chunked_data_from_generator(): Applies a given function to each chunk in the generator.

- utils/**csv_generator.py**: Generator for reading large CSVs in chunks.
    - csv_chunk_generator(): Yields chunks from a CSV based on config settings.

# src/utils/

- Logging (utils/log_helper.py): Logs processes and errors to a file and console for debugging.
- plotting (utils/plot_helper.py): Creates visualizations like bar charts, histograms, etc.
- safe_open (utils/safe_open.py): Safely opens files with error handling for common file issues.

## Usage

### Running the Playtime vs. Sentiment Analysis

The project is set up to run this assignment from src/main.py

The analysis is run from big_data/main.py, which initializes the playtime vs. sentiment analysis:

        python

        import os
        from big_data.analysis import playtime_vs_sentiment
        import matplotlib.pyplot as plt
        
        playtime_vs_sentiment.prepare_data_chunks()
        playtime_vs_sentiment.chart_data()
        plt.show()

### Creating a New Analysis

- Duplicate the analysis_template.py and update config.
- Define compute_aggregated_metrics() and chart_data() for your analysis.

Each analysis file will only need to configure settings and define computation logic for metrics and/or charts.
