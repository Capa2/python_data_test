import os
import csv
import pandas as pd
from big_data.generators import csv_generator
from big_data.generators.use_generator import use_generator
from utils.safe_open import safe_open
from utils.logger import get_logger

# Logger setup
LOGGER = get_logger("data_processing.log")

def initialize_output(config):
    LOGGER.info("Starting data processing. Clearing the output file.")
    try:
        with safe_open(config['write_path'], mode='w', encoding="utf-8-sig", newline='') as file:
            pass
    except Exception as e:
        LOGGER.error(f"Error clearing the output file: {e}")

def process_data(config):
    initialize_output(config)
    try:
        csv_chunk_generator = csv_generator.csv_chunk_generator(config)
        LOGGER.info("CSV generator initialized. Processing chunks.")
        use_generator(generator=csv_chunk_generator, func=append_chunk, config=config)
    except FileNotFoundError:
        LOGGER.error(f"File not found: {config['read_path']}")
    except Exception as e:
        LOGGER.error(f"Unexpected error during data processing: {e}")

def append_chunk(i, chunk, config):
    LOGGER.info(f"Processing chunk {i + 1}")
    rows = chunk if config['row_per_chunk'] in [0, None] else chunk.head(config['row_per_chunk'])
    try:
        with safe_open(config['write_path'], mode='a', encoding="utf-8-sig", newline='') as file:
            writer = csv.writer(file, delimiter=config['delimiter'])
            if i == 0:
                LOGGER.info("Writing headers to the output file.")
                writer.writerow(process_headers(rows.columns, config))
            writer.writerows(process_rows(rows, config))
            LOGGER.info(f"Appended {len(rows)} rows from chunk {i + 1} to {config['write_path']}")
    except Exception as e:
        LOGGER.error(f"Error writing chunk {i + 1} to the output file: {e}")

def process_headers(headers, config):
    return headers

def process_rows(rows, config):
    if 'language_filter' in config and config['language_filter']:
        rows = rows[rows['language'].str.lower() == config['language_filter'].str.lower()]
    return rows.values.tolist()