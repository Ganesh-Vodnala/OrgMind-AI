from pathlib import Path
import shutil

from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.capture.capture_request import CaptureDocumentRequest
from app.schemas.knowledge_source import KnowledgeSourceResponse
from app.services.capture.capture_service import CaptureService

router = APIRouter(
    prefix="/capture",
    tags=["Capture"]
)

UPLOAD_DIR = Path("uploads/temp")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/document",  response_model=KnowledgeSourceResponse)
def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    # Save uploaded file
    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Create request object
    request = CaptureDocumentRequest(
        file_path=str(file_path),
        original_filename=file.filename
    )

    # Process document
    capture_service = CaptureService(db)
    knowledge_source = capture_service.capture_document(request)

    return knowledge_source