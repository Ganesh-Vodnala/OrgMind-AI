from dataclasses import dataclass, field
from typing import List, Optional

from app.engines.processing.models.entity import Entity


@dataclass
class TextChunk:

    content: str

    chunk_index: int

    start_offset: int

    end_offset: int

    metadata: Optional[dict] = None

    entities: List[Entity] = field(
        default_factory=list
    )
    embedding: List[float] | None = None