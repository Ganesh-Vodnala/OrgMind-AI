import re
from typing import List

from app.engines.processing.models.entity import Entity
from app.engines.processing.models.relationship import Relationship

from app.engines.processing.relationship_extractors.base.base_relationship_extractor import (
    BaseRelationshipExtractor
)


class BasicRelationshipExtractor(BaseRelationshipExtractor):

    RELATIONSHIP_PATTERNS = {
        "USES": r"\buses\b",
        "USED_BY": r"\bused by\b",
        "DEPENDS_ON": r"\bdepends on\b",
        "DESIGNED": r"\bdesigned\b",
        "CREATED": r"\bcreated\b",
        "OWNS": r"\bowns\b",
        "MAINTAINS": r"\bmaintains\b",
    }

    def extract(
        self,
        text: str,
        entities: List[Entity]
    ) -> List[Relationship]:

        relationships = []

        if not text.strip():
            return relationships

        if not entities:
            return relationships

        for sentence_match in re.finditer(
            r"[^.!?]+[.!?]?",
            text
        ):

            sentence = sentence_match.group().strip()

            if not sentence:
                continue

            sentence_start = sentence_match.start()

            sentence_entities = []

            for entity in entities:

                if (
                    entity.start_offset >= sentence_start
                    and entity.end_offset <=
                    sentence_start + len(sentence)
                ):
                    sentence_entities.append(entity)

            if len(sentence_entities) < 2:
                continue

            sentence_entities.sort(
                key=lambda entity: entity.start_offset
            )

            for relationship_type, pattern in self.RELATIONSHIP_PATTERNS.items():

                match = re.search(
                    pattern,
                    sentence,
                    re.IGNORECASE
                )

                if not match:
                    continue

                before = [
                    entity
                    for entity in sentence_entities
                    if entity.end_offset <=
                    sentence_start + match.start()
                ]

                after = [
                    entity
                    for entity in sentence_entities
                    if entity.start_offset >=
                    sentence_start + match.end()
                ]

                if not before or not after:
                    continue

                source_entity = before[-1]
                target_entity = after[0]

                if relationship_type == "USED_BY":

                    source_entity, target_entity = (
                        target_entity,
                        source_entity
                    )

                evidence = sentence

                relationships.append(
                    Relationship(
                        source_entity=source_entity,
                        target_entity=target_entity,
                        relationship_type=relationship_type,
                        evidence=evidence
                    )
                )

                break

        return relationships