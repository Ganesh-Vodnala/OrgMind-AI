from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship

from app.database.base import Base


class TextChunk(Base):

    __tablename__ = "text_chunks"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    knowledge_source_id = Column(
        Integer,
        ForeignKey("knowledge_sources.id"),
        nullable=False
    )

    content = Column(
        Text,
        nullable=False
    )

    chunk_index = Column(
        Integer,
        nullable=False
    )

    start_offset = Column(
        Integer,
        nullable=False
    )

    end_offset = Column(
        Integer,
        nullable=False
    )
    knowledge_source = relationship(
        "KnowledgeSource",
        back_populates="chunks"
    )