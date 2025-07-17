from db_connection import get_db_connection
@app.get("/api/students")
async def get_students():
    conn = get_db_connection()
    if conn is None:
        return {"error": "Database connection failed"}
    
    try:
        df = pd.read_sql("SELECT * FROM students", conn)
        return df.to_dict('records')
    except Exception as e:
        return {"error": str(e)}
    finally:
        conn.close()