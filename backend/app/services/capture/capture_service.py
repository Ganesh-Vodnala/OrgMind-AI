from sqlalchemy.orm import Session

from app.engines.capture.collectors.document_collector import DocumentCollector
from app.schemas.capture.capture_request import CaptureDocumentRequest
from app.schemas.knowledge_source import KnowledgeSourceCreate
from app.services.knowledge_source_service import KnowledgeSourceService
from app.services.processing.processing_service import ProcessingService
from app.services.text_chunk_service import TextChunkService

class CaptureService:

    def __init__(self, db: Session):
        self.db = db
        self.document_collector = DocumentCollector()
        self.processing_service = ProcessingService()
        self.knowledge_source_service = KnowledgeSourceService()
        self.text_chunk_service = TextChunkService()

    def capture_document(self, request: CaptureDocumentRequest):
        capture_result = self.document_collector.collect(request.file_path)
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
        self.text_chunk_service.create_chunks(
            self.db,
            knowledge_source.id,
            processed_document.chunks
        )
        return knowledge_source