import app.models

from app.database.base import Base
from app.database.database import SessionLocal, engine

from app.models.knowledge_source import KnowledgeSource
from app.models.text_chunk import TextChunk
from app.models.entity import Entity
from app.models.entity_mention import EntityMention

from app.enums.source_type import SourceType

db = SessionLocal()

try:
    # Create a knowledge source
    knowledge_source = KnowledgeSource(
        title="Entity Test Document",
        source_type=SourceType.DOCUMENT,
        raw_content="Redis is used for caching. REDIS is fast."
    )

    db.add(knowledge_source)
    db.commit()
    db.refresh(knowledge_source)

    # Create a text chunk
    chunk = TextChunk(
        knowledge_source_id=knowledge_source.id,
        content="Redis is used for caching. REDIS is fast.",
        chunk_index=0,
        start_offset=0,
        end_offset=42
    )

    db.add(chunk)
    db.commit()
    db.refresh(chunk)

    # Create ONE logical entity
    entity = Entity(
        name="Redis",
        entity_type="TECHNOLOGY",
        canonical_name="redis"
    )

    db.add(entity)
    db.commit()
    db.refresh(entity)

    # Create first mention
    mention1 = EntityMention(
        entity_id=entity.id,
        text_chunk_id=chunk.id,
        text="Redis",
        start_offset=0,
        end_offset=5,
        confidence=1.0
    )

    # Create second mention
    mention2 = EntityMention(
        entity_id=entity.id,
        text_chunk_id=chunk.id,
        text="REDIS",
        start_offset=28,
        end_offset=33,
        confidence=0.95
    )

    db.add_all([mention1, mention2])
    db.commit()

    # Reload entity
    db.refresh(entity)

    print("Entity:")
    print("ID:", entity.id)
    print("Name:", entity.name)
    print("Type:", entity.entity_type)
    print("Canonical:", entity.canonical_name)

    print("\nMentions:")

    for mention in entity.mentions:
        print(
            mention.text,
            mention.start_offset,
            mention.end_offset
        )

    print("\n==============================")
    print("ENTITY PERSISTENCE TEST PASSED")
    print("==============================")

finally:
    db.close()