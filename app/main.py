from fastapi import FastAPI
from app.db import get_db_connection

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI + Docker + Postgres works!"}

@app.get("/db")
def test_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT 1;")
    result = cur.fetchone()
    conn.close()
    return {"db_response": result[0]}
