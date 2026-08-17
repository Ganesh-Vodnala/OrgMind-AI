from dataclasses import dataclass
from typing import Optional


@dataclass
class Entity:
    text: str
    entity_type: str
    start_offset: int
    end_offset: int
    confidence: Optional[float] = None