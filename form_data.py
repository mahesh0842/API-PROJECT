from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from db_connection import get_db_connection
import mysql.connector

app = FastAPI()

# Set up template rendering from templates/ folder
templates = Jinja2Templates(directory="templates")

# Home page route that serves the form.html using Jinja2 template
@app.get("/", response_class=HTMLResponse)
async def show_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

# POST route to submit form data
@app.post("/submit-student/")
async def submit_student(request: Request):
    data = await request.json()
    conn = get_db_connection()
    
    if not conn:
        return JSONResponse(
            {"message": "Failed to connect to database"},
            status_code=500
        )
    
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            INSERT INTO students 
            (student_id, first_name, last_name, email, date_of_birth,
             gender, major, gpa, enrollment_date, phone_number, address)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, 
            (
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
            )
        )
        conn.commit()
        return JSONResponse(
            {"message": "Student registered successfully!"}, 
            status_code=200
        )
    except mysql.connector.Error as err:
        conn.rollback()
        return JSONResponse(
            {"message": f"Database error: {err}"},
            status_code=400
        )
    except Exception as e:
        return JSONResponse(
            {"message": f"Error: {str(e)}"},
            status_code=400
        )
    finally:
        cursor.close()
        conn.close()

# Run the app on port 8001
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)