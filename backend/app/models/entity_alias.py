from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class EntityAlias(Base):

    __tablename__ = "entity_aliases"

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

    alias: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    canonical_alias: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    entity = relationship(
        "Entity",
        back_populates="aliases"
    )