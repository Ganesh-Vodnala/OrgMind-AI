import re


class EntityNormalizationService:

    @staticmethod
    def normalize(name: str) -> str:
        if not name:
            return ""

        normalized = name.strip().lower()

        normalized = re.sub(
            r"\s+",
            " ",
            normalized
        )

        return normalized