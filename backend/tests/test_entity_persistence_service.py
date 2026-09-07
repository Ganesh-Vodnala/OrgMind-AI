import app.models

from app.database.base import Base
from app.database.database import SessionLocal, engine

from app.models.knowledge_source import KnowledgeSource
from app.models.text_chunk import TextChunk

from app.engines.processing.models.text_chunk import (
    TextChunk as ProcessingTextChunk
)
from app.engines.processing.models.entity import Entity as ProcessingEntity

from app.services.entity_persistence_service import (
    EntityPersistenceService
)

from app.enums.source_type import SourceType


Base.metadata.create_all(bind=engine)

db = SessionLocal()

try:

    # Database knowledge source
    knowledge_source = KnowledgeSource(
        title="Persistence Test",
        source_type=SourceType.DOCUMENT,
        raw_content="Redis is used for caching. REDIS is fast."
    )

    db.add(knowledge_source)
    db.commit()
    db.refresh(knowledge_source)

    # Database text chunk
    db_chunk = TextChunk(
        knowledge_source_id=knowledge_source.id,
        content="Redis is used for caching. REDIS is fast.",
        chunk_index=0,
        start_offset=0,
        end_offset=42
    )

    db.add(db_chunk)
    db.commit()
    db.refresh(db_chunk)

    # Processing-layer entities
    processing_chunk = ProcessingTextChunk(
        content="Redis is used for caching. REDIS is fast.",
        chunk_index=0,
        start_offset=0,
        end_offset=42
    )

    processing_chunk.entities = [
        ProcessingEntity(
            text="Redis",
            entity_type="TECHNOLOGY",
            start_offset=0,
            end_offset=5
        ),
        ProcessingEntity(
            text="REDIS",
            entity_type="TECHNOLOGY",
            start_offset=28,
            end_offset=33
        )
    ]

    # Connect processing chunk to database chunk
    processing_chunk.id = db_chunk.id

    # Persist
    entities = EntityPersistenceService.persist_entities(
        db,
        [processing_chunk]
    )

    print("\nPersisted Entities:")

    for entity in entities:
        print(
            entity.id,
            entity.name,
            entity.canonical_name
        )

    # Verify both mentions
    persisted_entity = entities[0]

    db.refresh(persisted_entity)

    print("\nEntity Mentions:")

    for mention in persisted_entity.mentions:
        print(
            mention.text,
            mention.start_offset,
            mention.end_offset,
            "Entity ID:",
            mention.entity_id
        )

    # Assertions
    assert len(entities) == 2

    assert entities[0].id == entities[1].id

    assert len(persisted_entity.mentions) == 2

    assert {
        mention.text
        for mention in persisted_entity.mentions
    } == {"Redis", "REDIS"}

    print("\n==============================")
    print("ENTITY PERSISTENCE SERVICE TEST PASSED")
    print("==============================")

finally:
    db.close()