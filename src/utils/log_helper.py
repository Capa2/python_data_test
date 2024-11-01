# utils/log_helper.py

import logging
import os

log_dir = 'logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

def get_logger(filename):
    # Create logger with the specified name
    logger = logging.getLogger(filename)
    logger.setLevel(logging.INFO)  # Set the overall logging level

    # Create file handler to log to a file
    file_handler = logging.FileHandler(os.path.join(log_dir, filename + ".log"))
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    # Create console handler to print to console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    # Add handlers only if they are not already added (to prevent duplicates)
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger