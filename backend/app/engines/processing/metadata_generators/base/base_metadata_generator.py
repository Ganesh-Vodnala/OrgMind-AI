from abc import ABC, abstractmethod
from typing import List

from app.engines.processing.models.entity import Entity
from app.engines.processing.models.knowledge_metadata import KnowledgeMetadata
from app.engines.processing.models.relationship import Relationship


class BaseMetadataGenerator(ABC):

    @abstractmethod
    def generate(
        self,
        text: str,
        entities: List[Entity],
        relationships: List[Relationship]
    ) -> KnowledgeMetadata:
        pass