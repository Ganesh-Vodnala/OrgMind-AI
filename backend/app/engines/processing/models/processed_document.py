from dataclasses import dataclass, field
from typing import List

from app.engines.processing.models.text_chunk import TextChunk
from app.engines.processing.models.relationship import Relationship


@dataclass
class ProcessedDocument:

    cleaned_text: str

    chunks: List[TextChunk] = field(
        default_factory=list
    )

    relationships: List[Relationship] = field(
        default_factory=list
    )