from utils.logger import get_logger
from pandas.errors import ParserError, EmptyDataError

LOGGER = get_logger("gen_log")

def limit_reached(i, config):
    chunk_limit = config.get('chunk_limit')
    if chunk_limit is not None and chunk_limit > 0 and i >= chunk_limit:
        return True
    return False

def process_chunk(chunk, config):
    if config.get('filter_cols'):
        processed_chunk = chunk.dropna(subset=config['filter_cols'])
    else:
        processed_chunk = chunk.dropna()
    return processed_chunk

def use_generator(generator, func, config):
    try:
        for i, chunk in enumerate(generator):
            if limit_reached(i, config): break
            processed_chunk = process_chunk(chunk, config)
            func(i, processed_chunk, config)
        
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
