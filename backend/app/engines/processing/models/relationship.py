from dataclasses import dataclass
from typing import Optional

from app.engines.processing.models.entity import Entity


@dataclass
class Relationship:

    source_entity: Entity

    target_entity: Entity

    relationship_type: str

    confidence: Optional[float] = None

    evidence: Optional[str] = None