# test_db_connection.py
from db_connection import get_db_connection, close_db_connection

def test_connection():
    """Test the database connection and basic operations."""
    conn = None
    try:
        # Get connection
        conn = get_db_connection()
        if not conn:
            print("Failed to connect to database")
            return

        # Create cursor
        cursor = conn.cursor()
        
        # Execute a simple query
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        print(f"Database version: {version[0]}")

        # Close cursor
        cursor.close()

    except Exception as e:
        print(f"Error during database operation: {e}")
    finally:
        # Ensure connection is closed
        close_db_connection(conn)

if __name__ == "__main__":
    test_connection()
