
from contextlib import contextmanager
from utils.logger import get_logger
import re
import csv

LOGGER = get_logger("file_errors")

@contextmanager
def safe_open(path, mode='r', newline=None, encoding="utf-8-sig"):
    action = 'read' if mode == 'r' else 'write to' if mode == 'w' else 'append' if mode == 'a' else 'access'
    file = None
    try:
        file = open(path, mode, newline=newline, encoding=encoding)
        yield file
    except FileNotFoundError:
       LOGGER.error(f"File {path} was not found.")
       raise
    except PermissionError:
        action = 'read' if mode == 'r' else 'write to' if mode == 'w' else 'append' if mode == 'a' else 'access'
        LOGGER.error(f"Permission denied to {action} file: {path}.")
        raise
    except ValueError:
        LOGGER.error(f"Invalid file mode: {mode}. Valid options are 'r', 'w' and 'a'")
        raise
    except IOError as e:  # Handle any general I/O error (writing, disk issues, etc.)
        LOGGER.error(f"I/O error occurred while trying to {action} {path}: {e}")
        raise
    except Exception as e:
        LOGGER.error(f"An unexpected error occurred: {e}")
        raise
    finally:
        if file is not None:
            file.close()