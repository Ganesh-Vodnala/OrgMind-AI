from dataclasses import dataclass, field
from typing import List

from app.engines.processing.models.text_chunk import TextChunk


@dataclass
class ProcessedDocument:

    cleaned_text: str

    chunks: List[TextChunk] = field(default_factory=list)