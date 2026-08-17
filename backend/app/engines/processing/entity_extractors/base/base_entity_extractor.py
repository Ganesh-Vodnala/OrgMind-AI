from abc import ABC, abstractmethod
from typing import List

from app.engines.processing.models.entity import Entity


class BaseEntityExtractor(ABC):

    @abstractmethod
    def extract(self, text: str) -> List[Entity]:
        pass