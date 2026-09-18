from sqlalchemy.orm import Session

from app.models.entity_alias import EntityAlias
from app.services.entity_normalization_service import (
    EntityNormalizationService
)


class EntityAliasRepository:

    @staticmethod
    def find_by_canonical_alias(
        db: Session,
        canonical_alias: str
    ) -> EntityAlias | None:

        return (
            db.query(EntityAlias)
            .filter(
                EntityAlias.canonical_alias == canonical_alias
            )
            .first()
        )

    @staticmethod
    def create(
        db: Session,
        entity_id: int,
        alias: str
    ) -> EntityAlias:

        canonical_alias = EntityNormalizationService.normalize(
            alias
        )

        entity_alias = EntityAlias(
            entity_id=entity_id,
            alias=alias,
            canonical_alias=canonical_alias
        )

        db.add(entity_alias)
        db.commit()
        db.refresh(entity_alias)

        return entity_alias