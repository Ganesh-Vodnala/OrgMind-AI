from abc import ABC, abstractmethod

from app.engines.processing.models.knowledge_classification import (
    KnowledgeClassification
)


class BaseKnowledgeClassifier(ABC):

    @abstractmethod
    def classify(
        self,
        text: str
    ) -> KnowledgeClassification:
        pass