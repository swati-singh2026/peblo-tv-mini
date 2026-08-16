from fastapi import FastAPI
from sqlalchemy import text

from app.db.session import engine

app = FastAPI(title="Peblo TV API")


@app.get("/")
def root():
    return {"message": "Peblo TV Backend Running 🚀"}


@app.get("/health")
def health():
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))

    return {
        "status": "healthy",
        "database": "connected"
    }