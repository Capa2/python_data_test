# big_data/utils/apply_to_chunked_data_from_generator.py

from utils.log_helper import get_logger
from pandas.errors import ParserError, EmptyDataError

LOGGER = get_logger("generator_log")

def is_chunk_limit_reached(i, config):
    chunk_limit = config.get('chunk_limit')
    if chunk_limit is not None and chunk_limit > 0 and i >= chunk_limit:
        return True
    return False

def filter_chunk_data(chunk, config):
    if config.get('filter_cols'):
        return chunk.dropna(subset=config['filter_cols'])
    return chunk

def apply_to_chunked_data_from_generator(generator, func, config):
    try:
        for i, chunk in enumerate(generator):
            if is_chunk_limit_reached(i, config): break
            filtered_chunk = filter_chunk_data(chunk, config)
            func(i, filtered_chunk, config)
        
    except StopIteration:
        LOGGER.warning("Generator exhausted or no data found.")
        
    except FileNotFoundError:
        LOGGER.error("The specified file was not found.")
        
    except EmptyDataError:
        LOGGER.error("The CSV file is empty.")
        
    except ParserError:
        LOGGER.error("There was an error parsing the CSV file. Check for malformed rows.")
        
    except TypeError as e:
        LOGGER.error(f"TypeError encountered with callback function: {e}")
