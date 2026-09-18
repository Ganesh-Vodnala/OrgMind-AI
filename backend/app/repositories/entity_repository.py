from sqlalchemy.orm import Session

from app.models.entity import Entity
from app.services.entity_normalization_service import (
    EntityNormalizationService
)

class EntityRepository:

    @staticmethod
    def canonicalize(name: str) -> str:
        return EntityNormalizationService.normalize(name)

    @staticmethod
    def find_by_canonical_name(
        db: Session,
        canonical_name: str
    ) -> Entity | None:

        return (
            db.query(Entity)
            .filter(
                Entity.canonical_name == canonical_name
            )
            .first()
        )

    @staticmethod
    def create(
        db: Session,
        name: str,
        entity_type: str
    ) -> Entity:

        canonical_name = EntityRepository.canonicalize(name)

        entity = Entity(
            name=name,
            entity_type=entity_type,
            canonical_name=canonical_name
        )

        db.add(entity)
        db.commit()
        db.refresh(entity)

        return entity

    @staticmethod
    def get_or_create(
        db: Session,
        name: str,
        entity_type: str
    ) -> Entity:

        canonical_name = EntityRepository.canonicalize(name)

        existing_entity = (
            EntityRepository.find_by_canonical_name(
                db,
                canonical_name
            )
        )

        if existing_entity:
            return existing_entity

        return EntityRepository.create(
            db,
            name,
            entity_type
        )