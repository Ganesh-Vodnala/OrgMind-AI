from sqlalchemy.orm import Session

from app.models.entity import Entity
from app.models.entity_mention import EntityMention
from app.models.text_chunk import TextChunk
from app.repositories.entity_repository import EntityRepository
from app.services.entity_resolution_service import (
    EntityResolutionService
)


class EntityPersistenceService:

    @staticmethod
    def persist_entities(
        db: Session,
        processing_chunks,
        db_chunks: list[TextChunk]
    ) -> list[Entity]:

        persisted_entities = []

        # Create a mapping:
        # processing chunk index → database TextChunk
        db_chunk_map = {
            chunk.chunk_index: chunk
            for chunk in db_chunks
        }

        for processing_chunk in processing_chunks:

            db_chunk = db_chunk_map.get(
                processing_chunk.chunk_index
            )

            if db_chunk is None:
                continue

            for extracted_entity in processing_chunk.entities:

                entity = EntityResolutionService.resolve(
                    db=db,
                    name=extracted_entity.text,
                    entity_type=extracted_entity.entity_type
                )
                if entity is None:
                    entity = EntityRepository.create(
                    db=db,
                    name=extracted_entity.text,
                    entity_type=extracted_entity.entity_type
                    )
                mention = EntityMention(
                    entity_id=entity.id,
                    text_chunk_id=db_chunk.id,
                    text=extracted_entity.text,
                    start_offset=extracted_entity.start_offset,
                    end_offset=extracted_entity.end_offset,
                    confidence=extracted_entity.confidence
                )

                db.add(mention)

                persisted_entities.append(entity)

        db.commit()

        return persisted_entities