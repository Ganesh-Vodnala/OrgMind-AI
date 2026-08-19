from dataclasses import dataclass


@dataclass
class KnowledgeClassification:

    knowledge_type: str

    confidence: float