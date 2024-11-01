# big_data/utils/data_writer.py

import csv
from big_data.utils.csv_reader import read_csv_in_chunks
from big_data.utils.chunk_processor import chunk_processor
from utils.safe_open import safe_open
from utils.log_helper import get_logger

# Logger setup
LOGGER = get_logger("data_processing")

def initialize_output_file(config):
    LOGGER.info("Starting data processing. Clearing the output file.")
    try:
        with safe_open(config['preprocessed_data_path'], mode='w', encoding="utf-8-sig", newline='') as file:
            pass
    except Exception as e:
        LOGGER.error(f"Error clearing the output file: {e}")

def write_chunks_to_preprocessed_file(config):
    initialize_output_file(config)
    try:
        csv_chunk_generator = read_csv_in_chunks(config)
        LOGGER.info("CSV generator initialized. Writing chunks to file.")

        chunk_processor(
            generator=csv_chunk_generator,
            process_func=transform_and_append_chunk,
            config=config
        )
    except FileNotFoundError:
        LOGGER.error(f"File not found: {config['source_data_path']}")
    except Exception as e:
        LOGGER.error(f"Unexpected error during data writing: {e}")

def transform_and_append_chunk(i, chunk, config):
    LOGGER.info(f"Processing chunk {i + 1}")
    rows = chunk if config['chunk_row_limit'] in [0, None] else chunk.head(config['chunk_row_limit'])
    try:
        with safe_open(config['preprocessed_data_path'], mode='a', encoding="utf-8-sig", newline='') as file:
            writer = csv.writer(file, delimiter=config['delimiter'])
            if i == 0:
                LOGGER.info("Writing headers to the output file.")
                writer.writerow(transform_headers(rows.columns, config))
            writer.writerows(transform_rows(rows, config))
            LOGGER.info(f"Appended {len(rows)} rows from chunk {i + 1} to {config['preprocessed_data_path']}")
    except Exception as e:
        LOGGER.error(f"Error writing chunk {i + 1} to the output file: {e}")

def transform_headers(headers, config):
    return headers

def transform_rows(rows, config):
    if 'lang_filter' in config and config['lang_filter']:
        rows = rows[rows['language'].str.lower() == config['lang_filter'].str.lower()]
    return rows.values.tolist()
