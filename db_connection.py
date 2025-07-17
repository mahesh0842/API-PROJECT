# db_connection.py
import mysql.connector

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Alpha@9655",
            database="connect"
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        return 
