# big_data/utils/chunk_processor.py

import inspect
from utils.log_helper import get_logger
from pandas.errors import ParserError, EmptyDataError

LOGGER = get_logger("chunk_processor_log")

def is_chunk_limit_reached(i, config=None):
    if config == None: return False
    chunk_limit = config.get('chunk_limit')
    return chunk_limit is not None and chunk_limit > 0 and i >= chunk_limit

def filter_chunk_data(chunk, config=None):
    if config == None: return chunk
    return chunk.dropna(subset=config['filter_cols']) if config.get('filter_cols') else chunk

def chunk_processor(generator, process_func, aggregate_func=None, config=None):
    partial_results = [] if aggregate_func else None

    try:
        for i, chunk in enumerate(generator):
            if is_chunk_limit_reached(i, config): break
            filtered_chunk = filter_chunk_data(chunk, config)

            if 'config' in inspect.signature(process_func).parameters:
                result = process_func(filtered_chunk, config)
            else:
                result = process_func(filtered_chunk)

            if aggregate_func:
                partial_results.append(result)
            else:
                LOGGER.info(f"Processing chunk {i + 1}")

        if aggregate_func and partial_results:
            if 'config' in inspect.signature(aggregate_func).parameters:
                final_result = aggregate_func(partial_results, config)
            else:
                final_result = aggregate_func(partial_results)
                
            LOGGER.info("Aggregation complete.")
            return final_result

    except (StopIteration, FileNotFoundError, EmptyDataError, ParserError, TypeError) as e:
        LOGGER.error(f"Error during {'aggregation' if aggregate_func else 'processing'}: {e}")

    return None