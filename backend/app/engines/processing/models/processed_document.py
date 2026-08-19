from dataclasses import dataclass, field
from typing import List

from app.engines.processing.models.text_chunk import TextChunk
from app.engines.processing.models.relationship import Relationship
from app.engines.processing.models.knowledge_metadata import KnowledgeMetadata
from app.engines.processing.models.knowledge_classification import (
    KnowledgeClassification
)


@dataclass
class ProcessedDocument:

    cleaned_text: str

    chunks: List[TextChunk] = field(
        default_factory=list
    )

    relationships: List[Relationship] = field(
        default_factory=list
    )

    metadata: KnowledgeMetadata = field(
        default_factory=KnowledgeMetadata
    )

    classification: KnowledgeClassification = field(
        default_factory=lambda: KnowledgeClassification(
            knowledge_type="UNKNOWN",
            confidence=0.0
        )
    )