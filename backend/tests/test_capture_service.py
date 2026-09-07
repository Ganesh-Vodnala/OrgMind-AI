from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.services.capture.capture_service import CaptureService
from app.schemas.capture.capture_request import CaptureDocumentRequest


def test_capture_document_persists_entities():

    db: Session = SessionLocal()

    try:
        service = CaptureService(db)

        request = CaptureDocumentRequest(
        file_path=r"C:\Projects\OrgMind-AI\backend\uploads\temp\MY_RESUME.pdf",
        original_filename="MY_RESUME.pdf"
        )

        knowledge_source = service.capture_document(request)

        assert knowledge_source.id is not None

        print("\nKnowledge Source:")
        print(
            knowledge_source.id,
            knowledge_source.title
        )

        print("\n==============================")
        print("CAPTURE INTEGRATION TEST PASSED")
        print("==============================")

    finally:
        db.close()


if __name__ == "__main__":
    test_capture_document_persists_entities()