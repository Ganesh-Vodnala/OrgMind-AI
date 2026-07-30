from abc import ABC, abstractmethod
from typing import List

from app.engines.processing.models.text_chunk import TextChunk


class BaseChunker(ABC):

    @abstractmethod
    def chunk(self, text: str) -> List[TextChunk]:
        pass