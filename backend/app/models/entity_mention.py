from sqlalchemy import ForeignKey, Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class EntityMention(Base):

    __tablename__ = "entity_mentions"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    entity_id: Mapped[int] = mapped_column(
        ForeignKey("entities.id"),
        nullable=False,
        index=True
    )

    text_chunk_id: Mapped[int] = mapped_column(
        ForeignKey("text_chunks.id"),
        nullable=False,
        index=True
    )

    text: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    start_offset: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    end_offset: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    confidence: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )

    entity = relationship(
        "Entity",
        back_populates="mentions"
    )

    text_chunk = relationship(
        "TextChunk",
        back_populates="entity_mentions"
    )