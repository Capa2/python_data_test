# big_data/csv_reader.py

import pandas as pd

def read_csv_in_chunks(config):
    for chunk in pd.read_csv(
        config['source_data_path'], 
        chunksize=config['chunk_size'], 
        usecols=config['filter_cols'],
        delimiter=config['delimiter']
    ):
        yield chunk