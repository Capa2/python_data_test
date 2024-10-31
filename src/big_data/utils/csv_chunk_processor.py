# big_data/utils/csv_chunk_processor.py

import csv
from big_data.utils import csv_generator
from big_data.utils.apply_to_chunked_data_from_generator import apply_to_chunked_data_from_generator
from utils.safe_open import safe_open
from utils.log_helper import get_logger

# Logger setup
LOGGER = get_logger("data_processing.log")

def clear_output_file(config):
    LOGGER.info("Starting data processing. Clearing the output file.")
    try:
        with safe_open(config['aggregated_data_path'], mode='w', encoding="utf-8-sig", newline='') as file:
            pass
    except Exception as e:
        LOGGER.error(f"Error clearing the output file: {e}")

def process_csv(config):
    clear_output_file(config)
    try:
        csv_chunk_generator = csv_generator.csv_chunk_generator(config)
        LOGGER.info("CSV generator initialized. Processing chunks.")
        apply_to_chunked_data_from_generator(generator=csv_chunk_generator, func=write_chunk_to_file, config=config)
    except FileNotFoundError:
        LOGGER.error(f"File not found: {config['source_data_path']}")
    except Exception as e:
        LOGGER.error(f"Unexpected error during data processing: {e}")

def write_chunk_to_file(i, chunk, config):
    LOGGER.info(f"Processing chunk {i + 1}")
    rows = chunk if config['row_per_chunk'] in [0, None] else chunk.head(config['row_per_chunk']) # Write the whole chunk unless rows per chunk is defined
    try:
        with safe_open(config['aggregated_data_path'], mode='a', encoding="utf-8-sig", newline='') as file: # Append each chunk to output with encoding signature to support non-latin characters
            writer = csv.writer(file, delimiter=config['delimiter'])
            if i == 0:
                LOGGER.info("Writing headers to the output file.")
                writer.writerow(transform_headers(rows.columns, config))
            writer.writerows(transform_rows(rows, config))
            LOGGER.info(f"Appended {len(rows)} rows from chunk {i + 1} to {config['aggregated_data_path']}")
    except Exception as e:
        LOGGER.error(f"Error writing chunk {i + 1} to the output file: {e}")

def transform_headers(headers, config):
    return headers

def transform_rows(rows, config):
    if 'lang_filter' in config and config['lang_filter']:
        rows = rows[rows['language'].str.lower() == config['lang_filter'].str.lower()]
    return rows.values.tolist()