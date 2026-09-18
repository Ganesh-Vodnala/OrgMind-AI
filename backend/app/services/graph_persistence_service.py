from typing import List

from app.models.entity import Entity
from app.models.relationship import Relationship
from app.repositories.neo4j_repository import Neo4jRepository


class GraphPersistenceService:

    def __init__(self):

        self.neo4j_repository = Neo4jRepository()

    def persist_entities(
        self,
        entities: List[Entity]
    ):

        for entity in entities:

            self.neo4j_repository.upsert_entity(
                name=entity.name,
                entity_type=entity.entity_type
            )

    def persist_relationships(
        self,
        relationships: List[Relationship]
    ):

        for relationship in relationships:

            self.neo4j_repository.upsert_relationship(
                source_name=relationship.source_entity.name,
                source_type=relationship.source_entity.entity_type,
                target_name=relationship.target_entity.name,
                target_type=relationship.target_entity.entity_type,
                relationship_type=relationship.relationship_type,
                confidence=relationship.confidence,
                evidence=relationship.evidence
            )

    def close(self):

        self.neo4j_repository.close()