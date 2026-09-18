from sqlalchemy.orm import Session

from app.models.entity import Entity
from app.repositories.entity_repository import EntityRepository
from app.repositories.entity_alias_repository import EntityAliasRepository
from app.services.entity_normalization_service import (
    EntityNormalizationService
)


class EntityResolutionService:

    @staticmethod
    def resolve(
        db: Session,
        name: str,
        entity_type: str
    ) -> Entity | None:

        canonical_name = EntityNormalizationService.normalize(
            name
        )

        if not canonical_name:
            return None

        # 1. Try exact canonical-name match
        entity = EntityRepository.find_by_canonical_name(
            db,
            canonical_name
        )

        if entity is not None:
            return entity

        # 2. Try alias match
        alias = EntityAliasRepository.find_by_canonical_alias(
            db,
            canonical_name
        )

        if alias is not None:
            return alias.entity

        # 3. No confident resolution
        return None