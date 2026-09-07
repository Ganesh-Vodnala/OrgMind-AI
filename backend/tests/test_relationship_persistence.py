from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.services.processing.processing_service import ProcessingService
from app.services.entity_persistence_service import EntityPersistenceService
from app.services.relationship_persistence_service import (
    RelationshipPersistenceService
)
from app.services.text_chunk_service import TextChunkService
from app.services.knowledge_source_service import KnowledgeSourceService

from app.schemas.knowledge_source import KnowledgeSourceCreate
from app.enums.source_type import SourceType


TEST_TEXT = """
Rajesh designed the Authentication Service.
The Authentication Service uses Redis.
"""


def test_relationship_persistence():

    db: Session = SessionLocal()

    try:
        # -----------------------------
        # 1. Process test text
        # -----------------------------

        processing_service = ProcessingService()

        processed_document = processing_service.process(
            TEST_TEXT
        )

        print("\n==============================")
        print("PROCESSED RELATIONSHIPS")
        print("==============================")

        for relationship in processed_document.relationships:
            print(
                f"{relationship.source_entity.text} "
                f"-> {relationship.relationship_type} "
                f"-> {relationship.target_entity.text}"
            )

        assert len(processed_document.relationships) > 0

        # -----------------------------
        # 2. Create knowledge source
        # -----------------------------

        knowledge_source_service = KnowledgeSourceService()

        knowledge_source = knowledge_source_service.create(
            db,
            KnowledgeSourceCreate(
                title="Relationship Persistence Test",
                source_type=SourceType.DOCUMENT,
                raw_content=processed_document.cleaned_text
            )
        )

        # -----------------------------
        # 3. Persist chunks
        # -----------------------------

        text_chunk_service = TextChunkService()

        db_chunks = text_chunk_service.create_chunks(
            db,
            knowledge_source.id,
            processed_document.chunks
        )

        # -----------------------------
        # 4. Persist entities
        # -----------------------------

        entity_persistence_service = EntityPersistenceService()

        entity_persistence_service.persist_entities(
            db,
            processed_document.chunks,
            db_chunks
        )

        # -----------------------------
        # 5. Persist relationships
        # -----------------------------

        relationship_persistence_service = (
            RelationshipPersistenceService()
        )

        persisted_relationships = (
            relationship_persistence_service.persist_relationships(
                db,
                processed_document.relationships
            )
        )

        # -----------------------------
        # 6. Verify
        # -----------------------------

        print("\n==============================")
        print("PERSISTED RELATIONSHIPS")
        print("==============================")

        for relationship in persisted_relationships:
            print(
                f"{relationship.source_entity_id} "
                f"-> {relationship.relationship_type} "
                f"-> {relationship.target_entity_id}"
            )

        assert len(persisted_relationships) == len(
            processed_document.relationships
        )

        print("\n==============================")
        print("RELATIONSHIP PERSISTENCE TEST PASSED")
        print("==============================")

    finally:
        db.close()


if __name__ == "__main__":
    test_relationship_persistence()