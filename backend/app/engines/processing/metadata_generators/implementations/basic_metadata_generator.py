from typing import List

from app.engines.processing.metadata_generators.base.base_metadata_generator import (
    BaseMetadataGenerator
)

from app.engines.processing.models.entity import Entity
from app.engines.processing.models.knowledge_metadata import KnowledgeMetadata
from app.engines.processing.models.relationship import Relationship


class BasicMetadataGenerator(BaseMetadataGenerator):

    def generate(
        self,
        text: str,
        entities: List[Entity],
        relationships: List[Relationship]
    ) -> KnowledgeMetadata:

        tags = []

        for entity in entities:

            if entity.text not in tags:
                tags.append(entity.text)

        knowledge_type = self._determine_knowledge_type(
            relationships
        )

        importance = self._determine_importance(
            relationships
        )

        return KnowledgeMetadata(
            knowledge_type=knowledge_type,
            importance=importance,
            tags=tags
        )

    def _determine_knowledge_type(
        self,
        relationships: List[Relationship]
    ) -> str:

        relationship_types = {
            relationship.relationship_type
            for relationship in relationships
        }

        if (
            "DESIGNED" in relationship_types
            or "DEPENDS_ON" in relationship_types
        ):
            return "TECHNICAL"

        if "USES" in relationship_types:
            return "TECHNICAL"

        return "GENERAL"

    def _determine_importance(
        self,
        relationships: List[Relationship]
    ) -> str:

        if len(relationships) >= 3:
            return "HIGH"

        if len(relationships) >= 1:
            return "MEDIUM"

        return "LOW"