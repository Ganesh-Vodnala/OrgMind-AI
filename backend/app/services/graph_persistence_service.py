from typing import List

from app.engines.processing.models.entity import Entity
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
                name=entity.text,
                entity_type=entity.entity_type
            )

    def close(self):

        self.neo4j_repository.close()