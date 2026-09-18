from datetime import datetime

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Entity(Base):

    __tablename__ = "entities"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    entity_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    canonical_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    mentions = relationship(
        "EntityMention",
        back_populates="entity",
        cascade="all, delete-orphan"
    )
    aliases = relationship(
        "EntityAlias",
        back_populates="entity",
        cascade="all, delete-orphan"
    )
    outgoing_relationships = relationship(
    "Relationship",
    foreign_keys="Relationship.source_entity_id",
    back_populates="source_entity",
    cascade="all, delete-orphan"
    )

    incoming_relationships = relationship(
    "Relationship",
    foreign_keys="Relationship.target_entity_id",
    back_populates="target_entity",
    cascade="all, delete-orphan"
    )
    