from sqlalchemy.orm import Session

from app.models.relationship import Relationship
from app.repositories.relationship_repository import RelationshipRepository
from app.services.entity_resolution_service import (
    EntityResolutionService
)


class RelationshipPersistenceService:

    @staticmethod
    def persist_relationships(
        db: Session,
        processing_relationships
    ) -> list[Relationship]:

        persisted_relationships = []

        for processing_relationship in processing_relationships:

            source_entity = processing_relationship.source_entity
            target_entity = processing_relationship.target_entity

            source_db_entity = EntityResolutionService.resolve(
                db=db,
                name=source_entity.text,
                entity_type=source_entity.entity_type
            )

            target_db_entity = EntityResolutionService.resolve(
                db=db,
                name=target_entity.text,
                entity_type=target_entity.entity_type
            )

            if source_db_entity is None:
                continue

            if target_db_entity is None:
                continue

            relationship = RelationshipRepository.create(
                db=db,
                source_entity_id=source_db_entity.id,
                target_entity_id=target_db_entity.id,
                relationship_type=processing_relationship.relationship_type,
                confidence=processing_relationship.confidence,
                evidence=processing_relationship.evidence
            )

            persisted_relationships.append(relationship)

        return persisted_relationships