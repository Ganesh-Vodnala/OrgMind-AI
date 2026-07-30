from typing import List

from app.engines.processing.chunkers.base.base_chunker import BaseChunker
from app.engines.processing.models.text_chunk import TextChunk


class FixedSizeChunker(BaseChunker):
    """
    Splits text into fixed-size chunks while:
    - avoiding word breaks whenever possible
    - supporting configurable overlap
    """

    def __init__(self, chunk_size: int = 1000, overlap: int = 200):

        if chunk_size <= 0:
            raise ValueError("chunk_size must be greater than zero")

        if overlap < 0:
            raise ValueError("overlap cannot be negative")

        if overlap >= chunk_size:
            raise ValueError("overlap must be smaller than chunk_size")

        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(self, text: str) -> List[TextChunk]:

        # Return empty list for empty or whitespace-only text
        if not text.strip():
            return []

        chunks = []
        start = 0
        chunk_index = 0

        while start < len(text):

            end = self._find_chunk_end(text, start)

            content = text[start:end].strip()

            chunk = TextChunk(
                content=content,
                chunk_index=chunk_index,
                start_offset=start,
                end_offset=end
            )

            chunks.append(chunk)

            # Last chunk reached
            if end == len(text):
                break

            # Calculate next chunk start
            next_start = self._calculate_next_start(end)

            # Ensure we always move forward
            start = max(start + 1, next_start)

            chunk_index += 1

        return chunks

    def _find_chunk_end(self, text: str, start: int) -> int:

        # Tentative chunk end
        end = min(start + self.chunk_size, len(text))

        # Already reached document end
        if end == len(text):
            return end

        split = end

        # Search backwards for whitespace
        while split > start:

            if text[split].isspace():
                return split

            split -= 1

        # Fallback: no whitespace found
        return end

    def _calculate_next_start(self, end: int) -> int:
        return max(0, end - self.overlap)