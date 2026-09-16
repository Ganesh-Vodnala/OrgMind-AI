from sqlalchemy.orm import Session

from app.engines.capture.collectors.document_collector import DocumentCollector
from app.schemas.capture.capture_request import CaptureDocumentRequest
from app.schemas.knowledge_source import KnowledgeSourceCreate
from app.services.knowledge_source_service import KnowledgeSourceService
from app.services.processing.processing_service import ProcessingService
from app.services.text_chunk_service import TextChunkService
from app.services.entity_persistence_service import EntityPersistenceService
from app.services.relationship_persistence_service import (
    RelationshipPersistenceService
)
from app.services.graph_persistence_service import (
    GraphPersistenceService
)
from app.services.vector_store.qdrant_service import QdrantService



class CaptureService:

    def __init__(self, db: Session):
        self.db = db
        self.document_collector = DocumentCollector()
        self.processing_service = ProcessingService()
        self.knowledge_source_service = KnowledgeSourceService()
        self.text_chunk_service = TextChunkService()
        self.entity_persistence_service = EntityPersistenceService()
        self.relationship_persistence_service = (
            RelationshipPersistenceService()
        )
        self.graph_persistence_service = GraphPersistenceService()
        self.qdrant_service = QdrantService()
        self.qdrant_service.create_collection()

    def capture_document(self, request: CaptureDocumentRequest):

        capture_result = self.document_collector.collect(
            request.file_path
        )

        processed_document = self.processing_service.process(
            capture_result.content
        )

        # Step 2: Convert to KnowledgeSourceCreate
        knowledge_source_data = KnowledgeSourceCreate(
            title=capture_result.title,
            source_type=capture_result.source_type,
            raw_content=processed_document.cleaned_text
        )

        # Step 3: Save to database
        knowledge_source = self.knowledge_source_service.create(
            self.db,
            knowledge_source_data
        )

        db_chunks = self.text_chunk_service.create_chunks(
            self.db,
            knowledge_source.id,
            processed_document.chunks
        )

        # Step 4: Prepare chunks for Qdrant
        qdrant_chunks = []

        for processed_chunk, db_chunk in zip(
            processed_document.chunks,
            db_chunks
        ):
            qdrant_chunks.append(
                {
                    "chunk_id": db_chunk.id,
                    "knowledge_source_id": knowledge_source.id,
                    "chunk_index": processed_chunk.chunk_index,
                    "content": processed_chunk.content,
                    "embedding": processed_chunk.embedding
                }
            )

        # Step 5: Store embeddings in Qdrant
        self.qdrant_service.upsert_chunks(
            qdrant_chunks
        )

        self.entity_persistence_service.persist_entities(
            self.db,
            processed_document.chunks,
            db_chunks
        )
        entities = []

        for chunk in processed_document.chunks:
            entities.extend(chunk.entities)

        self.graph_persistence_service.persist_entities(
            entities
        )
        self.relationship_persistence_service.persist_relationships(
            self.db,
            processed_document.relationships
        )
        self.graph_persistence_service.persist_relationships(
        processed_document.relationships
        )
        return knowledge_source