from fastapi import FastAPI
import psycopg2

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI + PostgreSQL"}

@app.get("/db-check")
def db_check():
    try:
        conn = psycopg2.connect(
            dbname="demo",
            user="user",
            password="password",
            host="db",
            port=5432,
        )
        conn.close()
        return {"db_status": "connected"}
    except Exception as e:
        return {"db_status": "error", "details": str(e)}
