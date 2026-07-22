from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.knowledge_source import (
    KnowledgeSourceCreate,
    KnowledgeSourceResponse
)
from app.services.knowledge_source_service import KnowledgeSourceService

router = APIRouter(
    prefix="/knowledge-sources",
    tags=["Knowledge Sources"]
)


@router.post(
    "/",
    response_model=KnowledgeSourceResponse
)
def create_knowledge_source(
    data: KnowledgeSourceCreate,
    db: Session = Depends(get_db)
):
    return KnowledgeSourceService.create(
        db=db,
        data=data
    )