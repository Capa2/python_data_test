import logging
import os

log_dir = 'logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.basicConfig(
    filename=os.path.join(log_dir, 'errors.log'),
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_logger(filename):
    logging.basicConfig(
        filename=os.path.join(log_dir, filename),
        level=logging.ERROR,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(filename)