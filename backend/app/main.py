from fastapi import FastAPI
from sqlalchemy import text

from app.api.knowledge_source import router as knowledge_source_router
from app.database.base import Base
from app.database.database import engine
from app.models.knowledge_source import KnowledgeSource
app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(knowledge_source_router)


@app.get("/")
def home():
    return {"message": "Welcome to OrgMind AI"}


@app.get("/database-test")
def database_test():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        version = result.scalar()

    return {
        "database": "Connected",
        "postgres_version": version
    }