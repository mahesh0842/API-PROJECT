# FOR JSON DATA INSERTION
from db_connection import get_db_connection
import json

def insert_students_data(json_file):
    """Inserts student data from a JSON file into the database."""
    conn = get_db_connection()
    cursor = None
    try:
        if conn:
            cursor = conn.cursor()
            # Load and insert data
            with open(json_file) as f:
                students = json.load(f)
                for student in students:
                    cursor.execute("""
                        INSERT INTO students (
                            student_id, first_name, last_name, email, date_of_birth,
                            gender, major, gpa, enrollment_date, phone_number, address
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """,
                        (
                            student['student_id'],
                            student['first_name'],
                            student['last_name'],
                            student['email'],
                            student['date_of_birth'],
                            student['gender'],
                            student['major'],
                            student['gpa'],
                            student['enrollment_date'],
                            student['phone_number'],
                            student['address']
                        )
                    )
            conn.commit()
            print("All student data inserted successfully!")
    except Exception as err:
        print(f"Error inserting data: {err}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
#path = '/Users/maheshyadav/Downloads/API/SQL/students.json'
insert_students_data('/Users/maheshyadav/Downloads/SQL/students_details.json')
