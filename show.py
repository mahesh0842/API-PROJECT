import pandas as pd
from db_connection import get_db_connection

def show_students_data():
    """
    Displays student data from the database in a formatted pandas table.
    """
    conn = get_db_connection()
    if conn:
        try:
            # Read SQL query directly into a DataFrame
            df = pd.read_sql("SELECT * FROM students", conn)
            
            if not df.empty:
                print("\nSTUDENTS DATA:")
                # Display with index and border (similar to tabulate's grid)
                print(df.to_markdown(tablefmt="grid", index=False))
            else:
                print("No data found in students table")
                
        except Exception as err:
            print(f"Error fetching data: {err}")
        finally:
            if conn.is_connected():
                conn.close()

# Example usage
if __name__ == "__main__":
    show_students_data()