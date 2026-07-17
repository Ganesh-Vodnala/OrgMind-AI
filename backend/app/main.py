from fastapi import FastAPI
from sqlalchemy import text

from app.database.database import engine
from app.database.base import Base
app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {
        "message": "Welcome to OrgMind AI"
    }


@app.get("/database-test")
def database_test():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        version = result.scalar()

    return {
        "database": "Connected",
        "postgres_version": version
    }