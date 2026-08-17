from abc import ABC, abstractmethod
from typing import List

from app.engines.processing.models.entity import Entity
from app.engines.processing.models.relationship import Relationship


class BaseRelationshipExtractor(ABC):

    @abstractmethod
    def extract(
        self,
        text: str,
        entities: List[Entity]
    ) -> List[Relationship]:
        pass