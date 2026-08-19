from abc import ABC, abstractmethod

from typing import List


class BaseEmbeddingGenerator(ABC):

    @abstractmethod
    def generate(
        self,
        texts: List[str]
    ) -> List[List[float]]:
        pass