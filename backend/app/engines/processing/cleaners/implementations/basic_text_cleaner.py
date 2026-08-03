import re

from app.engines.processing.cleaners.base.base_cleaner import BaseCleaner


class BasicTextCleaner(BaseCleaner):

    def clean(self, text: str) -> str:

        text = self._normalize_line_endings(text)

        text = self._remove_extra_spaces(text)

        text = self._remove_extra_blank_lines(text)

        return text.strip()

    def _normalize_line_endings(self, text: str) -> str:
        return (
            text.replace("\r\n", "\n")
                .replace("\r", "\n")
        )

    def _remove_extra_spaces(self, text: str) -> str:
        return re.sub(r"[ \t]+", " ", text)

    def _remove_extra_blank_lines(self, text: str) -> str:
        return re.sub(r"\n{3,}", "\n\n", text)