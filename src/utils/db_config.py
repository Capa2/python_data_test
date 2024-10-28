from sqlalchemy import create_engine
import mysql.connector
from mysql.connector import Error
from utils.logger import get_logger

SQL_LOGGER = get_logger("sql_log")

SQL_DB_CONFIG = {
    'host': 'localhost',     # Update with your MySQL host
    'port': 3306, 
    'user': 'root', # Update with your MySQL username
    'password': 'root', # Update with your MySQL password
    'database': 'northwind'   # Update with your database name
}

def get_connection():
    try:
        connection = mysql.connector.connect(**SQL_DB_CONFIG)
        print("Connected to MySQL database")
        SQL_LOGGER.info("Connected to MySQL database")
        return connection
    except Error as e:
        print(f"Error: {e}")
        SQL_LOGGER.error(f"Error: {e}")
        return None

def get_engine():
    return create_engine('mysql+mysqlconnector://root:root@localhost/northwind')

def test_connection():
    try:
        connection = mysql.connector.connect(**SQL_DB_CONFIG)
        if connection.is_connected():
            print("Connected to MySQL database")
        connection.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")