# view.py
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse ,JSONResponse
from fastapi.templating import Jinja2Templates
from db_connection import get_db_connection
import mysql.connector

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# ✅ Home page route
@app.get("/", response_class=HTMLResponse)
async def show_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# ✅ VIEW STUDENTS DETAILS route           GET
@app.get("/view-students", response_class=HTMLResponse)
async def view_students(request: Request):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    return templates.TemplateResponse("view_students.html", {"request": request, "students": students})

# ✅ FORM FILL UP route
@app.get("/form", response_class=HTMLResponse)
async def show_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

# ✅ SUBMIT STUDENT route               POST
@app.post("/submit-student/")
async def submit_student(request: Request):
    try:
        data = await request.json()
        conn = get_db_connection()

        if not conn:
            return JSONResponse({"message": "Failed to connect to database"}, status_code=500)

        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO students 
            (student_id, first_name, last_name, email, date_of_birth,
             gender, major, gpa, enrollment_date, phone_number, address)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            data['student_id'],
            data['first_name'],
            data['last_name'],
            data['email'],
            data['date_of_birth'],
            data['gender'],
            data['major'],
            data['gpa'],
            data['enrollment_date'],
            data['phone_number'],
            data['address']
        ))

        conn.commit()
        return JSONResponse({"message": "Student registered successfully!"}, status_code=200)

    except mysql.connector.Error as err:
        return JSONResponse({"message": f"Database error: {err}"}, status_code=400)

    except Exception as e:
        return JSONResponse({"message": f"Error: {str(e)}"}, status_code=400)

    finally:
        try:
            if cursor: cursor.close()
            if conn: conn.close()
        except:
            pass


# ✅ UPDATE STUDENT route
@app.get("/update-student-form", response_class=HTMLResponse)
async def update_student_form(request: Request):
    return templates.TemplateResponse("update_student.html", {"request": request})
    return templates.TemplateResponse("update_student_form.html", {"request": request})

# ✅ UPDATE STUDENT route.                PUT
@app.put("/update-student/{student_id}")
async def update_student(student_id: int, request: Request):
    try:
        data = await request.json()
        print("Update Data:", data)  # ✅ Debug log

        conn = get_db_connection()
        if not conn:
            return JSONResponse({"message": "Failed to connect to database"}, status_code=500)

        cursor = conn.cursor()

        # Check if student exists
        cursor.execute("SELECT * FROM students WHERE student_id = %s", (student_id,))
        if cursor.fetchone() is None:
            return JSONResponse({"message": f"Student with ID {student_id} not found."}, status_code=404)

        # Perform the update
        cursor.execute("""
            UPDATE students SET
                first_name = %s,
                last_name = %s,
                email = %s,
                date_of_birth = %s,
                gender = %s,
                major = %s,
                gpa = %s,
                enrollment_date = %s,
                phone_number = %s,
                address = %s
            WHERE student_id = %s
        """, (
            data['first_name'],
            data['last_name'],
            data['email'],
            data['date_of_birth'],
            data['gender'],
            data['major'],
            data['gpa'],
            data['enrollment_date'],
            data['phone_number'],
            data['address'],
            student_id
        ))

        conn.commit()
        return JSONResponse({"message": f"Student ID {student_id} updated successfully."}, status_code=200)

    except mysql.connector.Error as err:
        if conn:
            conn.rollback()
        return JSONResponse({"message": f"MySQL Error: {err}"}, status_code=500)

    except Exception as e:
        return JSONResponse({"message": f"Unexpected Error: {str(e)}"}, status_code=500)

    finally:
        if cursor: cursor.close()
        if conn: conn.close()

# ✅ DELETE STUDENT FORM route
@app.get("/delete-student-form", response_class=HTMLResponse)
async def delete_student_form(request: Request):
    return templates.TemplateResponse("delete_student.html", {"request": request})

# ✅ DELETE STUDENT endpoint
@app.delete("/delete-student/{student_id}")
async def delete_student(student_id: int):
    try:
        conn = get_db_connection()
        if not conn:
            return JSONResponse({"message": "Failed to connect to database"}, status_code=500)

        cursor = conn.cursor()

        cursor.execute("SELECT * FROM students WHERE student_id = %s", (student_id,))
        if cursor.fetchone() is None:
            return JSONResponse({"message": f"Student with ID {student_id} not found."}, status_code=404)

        cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
        conn.commit()

        return JSONResponse({"message": f"Student ID {student_id} deleted successfully."}, status_code=200)

    except mysql.connector.Error as err:
        if conn:
            conn.rollback()
        return JSONResponse({"message": f"MySQL Error: {err}"}, status_code=500)

    except Exception as e:
        return JSONResponse({"message": f"Unexpected Error: {str(e)}"}, status_code=500)

    finally:
        if 'cursor' in locals() and cursor: cursor.close()
        if 'conn' in locals() and conn: conn.close()

# Optional: to run directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)