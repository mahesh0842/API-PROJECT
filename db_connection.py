import mysql.connector
from typing import Optional
from mysql.connector.connection import MySQLConnection

def get_db_connection() -> Optional[MySQLConnection]:
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Alpha@9655",
            database="connect"
        )
        print("Successfully connected to the database")
        return conn
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def close_db_connection(conn: Optional[MySQLConnection]) -> None:
    if conn and conn.is_connected():
        conn.close()
        print("Database connection closed")

# ✅ Run test when script is executed directly
if __name__ == "__main__":
    conn = get_db_connection()
    if conn:
        close_db_connection(conn)