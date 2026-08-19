from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class KnowledgeMetadata:

    author: Optional[str] = None

    project: Optional[str] = None

    module: Optional[str] = None

    knowledge_type: Optional[str] = None

    importance: Optional[str] = None

    tags: List[str] = field(
        default_factory=list
    )

    confidence: Optional[float] = None