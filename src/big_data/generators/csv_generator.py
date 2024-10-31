import pandas as pd

def csv_chunk_generator(config):
    for chunk in pd.read_csv(config['read_path'], chunksize=config['chunk_size'], usecols=config['filter_cols']):
        yield chunk