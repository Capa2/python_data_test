#pickes_chunk_generator.py
import os
import glob
import pickle

def pickles_chunk_generator(folder_path, chunk_size=10):
    file_pattern = os.path.join(folder_path, '*.pickle')
    file_iterator = glob.iglob(file_pattern)

    chunk_data = []

    for file_path in file_iterator:
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
            chunk_data.append(data)
        
        if len(chunk_data) == chunk_size:
            yield chunk_data
            chunk_data = []
    
    if chunk_data:
        yield chunk_data