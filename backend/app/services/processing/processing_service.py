from app.engines.processing.cleaners.implementations.basic_text_cleaner import (
    BasicTextCleaner
)

from app.engines.processing.chunkers.implementations.fixed_size_chunker import (
    FixedSizeChunker
)
from app.engines.processing.models.processed_document import ProcessedDocument

class ProcessingService:

    def __init__(self):

        self.cleaner = BasicTextCleaner()

        self.chunker = FixedSizeChunker()
    def process(self, text: str) -> ProcessedDocument:

        cleaned_text = self.cleaner.clean(text)

        chunks = self.chunker.chunk(cleaned_text)

        return ProcessedDocument(
            cleaned_text=cleaned_text,
            chunks=chunks
        )