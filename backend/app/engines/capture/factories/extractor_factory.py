from pathlib import Path

from app.engines.capture.extractors.pdf.pdf_extractor import PDFExtractor
from app.engines.capture.extractors.base.document_extractor import (
    DocumentExtractor,
)
from app.engines.capture.exceptions.document_exceptions import (
    UnsupportedDocumentTypeError,
)

class ExtractorFactory:
    """
    Factory for creating document extractors.
    """

    @staticmethod
    def get_extractor(file_path: str) -> DocumentExtractor:
        extension = Path(file_path).suffix.lower()

        if extension == ".pdf":
            return PDFExtractor()

        raise UnsupportedDocumentTypeError(
            f"No extractor found for document type: {extension}"
        )