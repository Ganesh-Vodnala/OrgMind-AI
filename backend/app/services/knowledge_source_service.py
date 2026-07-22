from sqlalchemy.orm import Session

from app.models.knowledge_source import KnowledgeSource
from app.schemas.knowledge_source import KnowledgeSourceCreate


class KnowledgeSourceService:

    @staticmethod
    def create(
        db: Session,
        data: KnowledgeSourceCreate
    ) -> KnowledgeSource:

        knowledge_source = KnowledgeSource(
            title=data.title,
            source_type=data.source_type,
            raw_content=data.raw_content
        )

        db.add(knowledge_source)
        db.commit()
        db.refresh(knowledge_source)

        return knowledge_source