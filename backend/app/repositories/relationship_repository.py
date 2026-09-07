from sqlalchemy.orm import Session

from app.models.relationship import Relationship


class RelationshipRepository:

    @staticmethod
    def create(
        db: Session,
        source_entity_id: int,
        target_entity_id: int,
        relationship_type: str,
        confidence: float | None = None,
        evidence: str | None = None
    ) -> Relationship:

        relationship = Relationship(
            source_entity_id=source_entity_id,
            target_entity_id=target_entity_id,
            relationship_type=relationship_type,
            confidence=confidence,
            evidence=evidence
        )

        db.add(relationship)
        db.commit()
        db.refresh(relationship)

        return relationship

    @staticmethod
    def find(
        db: Session,
        source_entity_id: int,
        target_entity_id: int,
        relationship_type: str
    ) -> Relationship | None:

        return (
            db.query(Relationship)
            .filter(
                Relationship.source_entity_id == source_entity_id,
                Relationship.target_entity_id == target_entity_id,
                Relationship.relationship_type == relationship_type
            )
            .first()
        )