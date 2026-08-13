import app.database.models

from app.database.base import Base
from app.database.database import SessionLocal,engine
from app.engines.processing.models.text_chunk import TextChunk as ProcessingTextChunk
from app.models.knowledge_source import KnowledgeSource
from app.services.text_chunk_service import TextChunkService
from app.enums.source_type import SourceType


Base.metadata.create_all(bind=engine)
db = SessionLocal()

try:
    # Create a temporary knowledge source
    knowledge_source = KnowledgeSource(
        title="Test Document",
        source_type=SourceType.DOCUMENT,
        raw_content="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    )

    db.add(knowledge_source)
    db.commit()
    db.refresh(knowledge_source)

    print("Knowledge Source ID:", knowledge_source.id)

    # Create processing chunks
    chunks = [
        ProcessingTextChunk(
            content="ABCDE",
            chunk_index=0,
            start_offset=0,
            end_offset=5
        ),
        ProcessingTextChunk(
            content="FGHIJ",
            chunk_index=1,
            start_offset=5,
            end_offset=10
        ),
        ProcessingTextChunk(
            content="KLMNO",
            chunk_index=2,
            start_offset=10,
            end_offset=15
        )
    ]

    # Save chunks
    saved_chunks = TextChunkService.create_chunks(
        db,
        knowledge_source.id,
        chunks
    )

    print("\nSaved chunks:")

    for chunk in saved_chunks:
        print(
            chunk.id,
            chunk.knowledge_source_id,
            chunk.content,
            chunk.chunk_index
        )

finally:
    db.close()