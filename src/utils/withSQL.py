from functools import wraps
import pandas as pd
from utils.log_helper import get_logger
from utils.db_config import get_connection, get_engine

SQL_LOGGER = get_logger("sql_log")

def withSQL(query, return_dataframe=True):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if return_dataframe:
                try:
                    engine = get_engine()  # Ensure function call with parentheses
                    result = pd.read_sql_query(query, engine)
                    return func(result, *args, **kwargs)
                except Exception as e:
                    SQL_LOGGER.error(f"An error occurred with SQLAlchemy: {e}")
                    return None
            else:
                connection = get_connection()
                if connection is None:
                    SQL_LOGGER.error("Failed to connect to the database.")
                    return None
                try:
                    cursor = connection.cursor()
                    cursor.execute(query)
                    if query.strip().upper().startswith("SELECT"):
                        result = cursor.fetchall()
                    else:
                        connection.commit()
                        result = "Query executed successfully."
                    cursor.close()
                    return func(result, *args, **kwargs)
                except Exception as e:
                    SQL_LOGGER.error(f"An error occurred with mysql.connector: {e}")
                    return None
                finally:
                    if connection.is_connected():
                        connection.close()
        return wrapper
    return decorator
