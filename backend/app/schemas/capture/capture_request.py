from pydantic import BaseModel
from typing import Optional


class CaptureDocumentRequest(BaseModel):
    file_path: str
    original_filename: str
    source_type: str = "DOCUMENT"
    uploaded_by: Optional[int] = None