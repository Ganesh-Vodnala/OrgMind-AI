from app.engines.processing.cleaners.implementations.basic_text_cleaner import (
    BasicTextCleaner
)

from app.engines.processing.chunkers.implementations.fixed_size_chunker import (
    FixedSizeChunker
)

from app.engines.processing.entity_extractors.implementations.basic_entity_extractor import (
    BasicEntityExtractor
)

from app.engines.processing.relationship_extractors.implementations.basic_relationship_extractor import (
    BasicRelationshipExtractor
)

from app.engines.processing.models.processed_document import ProcessedDocument


class ProcessingService:

    def __init__(self):

        self.cleaner = BasicTextCleaner()

        self.chunker = FixedSizeChunker()

        self.entity_extractor = BasicEntityExtractor()

        self.relationship_extractor = BasicRelationshipExtractor()

    def process(self, text: str) -> ProcessedDocument:

        # Step 1: Clean the text
        cleaned_text = self.cleaner.clean(text)

        # Step 2: Split text into chunks
        chunks = self.chunker.chunk(cleaned_text)

        # Step 3: Extract entities
        entities = self.entity_extractor.extract(
            cleaned_text
        )

        # Step 4: Attach entities to their chunks
        for chunk in chunks:

            for entity in entities:

                if (
                    entity.start_offset >= chunk.start_offset
                    and entity.end_offset <= chunk.end_offset
                ):
                    chunk.entities.append(entity)

        # Step 5: Extract relationships
        relationships = self.relationship_extractor.extract(
            cleaned_text,
            entities
        )

        # Step 6: Return complete processed document
        return ProcessedDocument(
            cleaned_text=cleaned_text,
            chunks=chunks,
            relationships=relationships
        )