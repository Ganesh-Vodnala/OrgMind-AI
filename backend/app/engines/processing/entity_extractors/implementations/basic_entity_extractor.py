import re
from typing import List

from app.engines.processing.entity_extractors.base.base_entity_extractor import (
    BaseEntityExtractor
)
from app.engines.processing.entity_extractors.dictionaries.entity_dictionary import (
    ENTITY_DICTIONARY
)
from app.engines.processing.models.entity import Entity


class BasicEntityExtractor(BaseEntityExtractor):

    def extract(self, text: str) -> List[Entity]:

        if not text:
            return []

        candidates = []

        for entity_type, entity_names in ENTITY_DICTIONARY.items():

            for entity_name in entity_names:

                pattern = re.compile(
                    rf"(?<!\w){re.escape(entity_name)}(?!\w)",
                    re.IGNORECASE
                )

                for match in pattern.finditer(text):

                    candidates.append(
                        (
                            match.start(),
                            match.end(),
                            match.group(),
                            entity_type
                        )
                    )

        selected = self._remove_overlapping_matches(
            candidates
        )

        selected.sort(
            key=lambda candidate: candidate[0]
        )

        return [
            Entity(
                text=match_text,
                entity_type=entity_type,
                start_offset=start,
                end_offset=end
            )
            for start, end, match_text, entity_type
            in selected
        ]

    def _remove_overlapping_matches(self, candidates):

        # Longer entities get priority when they overlap.
        candidates.sort(
            key=lambda candidate: (
                -(candidate[1] - candidate[0]),
                candidate[0]
            )
        )

        selected = []

        for candidate in candidates:

            start, end, _, _ = candidate

            overlaps = any(
                start < selected_end
                and end > selected_start
                for selected_start, selected_end, _, _
                in selected
            )

            if not overlaps:
                selected.append(candidate)

        return selected