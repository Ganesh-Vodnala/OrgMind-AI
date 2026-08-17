from typing import List

from app.engines.processing.chunkers.base.base_chunker import BaseChunker
from app.engines.processing.models.text_chunk import TextChunk


class FixedSizeChunker(BaseChunker):
    """
    Splits text into approximately fixed-size chunks.

    Features:
    - configurable chunk size
    - configurable overlap
    - avoids breaking words whenever possible
    - preserves exact text offsets
    - handles short and empty documents
    """

    def __init__(
        self,
        chunk_size: int = 1000,
        overlap: int = 200
    ):
        if chunk_size <= 0:
            raise ValueError(
                "chunk_size must be greater than zero"
            )

        if overlap < 0:
            raise ValueError(
                "overlap cannot be negative"
            )

        if overlap >= chunk_size:
            raise ValueError(
                "overlap must be smaller than chunk_size"
            )

        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(self, text: str) -> List[TextChunk]:

        if not text:
            return []

        chunks: List[TextChunk] = []

        start = 0
        chunk_index = 0

        while start < len(text):

            end = self._find_chunk_end(
                text,
                start
            )

            content = text[start:end]

            chunks.append(
                TextChunk(
                    content=content,
                    chunk_index=chunk_index,
                    start_offset=start,
                    end_offset=end
                )
            )

            if end == len(text):
                break

            start = self._calculate_next_start(end)

            chunk_index += 1

        return chunks

    def _find_chunk_end(
        self,
        text: str,
        start: int
    ) -> int:

        end = min(
            start + self.chunk_size,
            len(text)
        )

        # Document ends inside this chunk
        if end == len(text):
            return end

        # Search backwards for whitespace
        split = end

        while split > start:

            if text[split - 1].isspace():
                return split

            split -= 1

        # No whitespace found.
        # Allow splitting a long word.
        return end

    def _calculate_next_start(
        self,
        end: int
    ) -> int:

        return end - self.overlap