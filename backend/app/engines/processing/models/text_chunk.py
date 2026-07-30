from dataclasses import dataclass
from typing import Optional


@dataclass
class TextChunk:
    content: str
    chunk_index: int

    start_offset: Optional[int] = None
    end_offset: Optional[int] = None

    metadata: Optional[dict] = None