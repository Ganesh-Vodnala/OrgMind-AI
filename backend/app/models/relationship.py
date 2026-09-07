from sqlalchemy import Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Relationship(Base):
    __tablename__ = "relationships"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    source_entity_id: Mapped[int] = mapped_column(
        ForeignKey("entities.id"),
        nullable=False,
        index=True
    )

    target_entity_id: Mapped[int] = mapped_column(
        ForeignKey("entities.id"),
        nullable=False,
        index=True
    )

    relationship_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True
    )

    confidence: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )

    evidence: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    source_entity = relationship(
        "Entity",
        foreign_keys=[source_entity_id],
        back_populates="outgoing_relationships"
    )

    target_entity = relationship(
        "Entity",
        foreign_keys=[target_entity_id],
        back_populates="incoming_relationships"
    )