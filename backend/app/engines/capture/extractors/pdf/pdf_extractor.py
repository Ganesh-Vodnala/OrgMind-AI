import fitz

from app.engines.capture.extractors.base.document_extractor import (
    DocumentExtractor,
)
from app.engines.capture.exceptions.document_exceptions import (
    DocumentExtractionError,
)


class PDFExtractor(DocumentExtractor):
    """
    Extract plain text from PDF documents.
    """

    def extract_text(self, file_path: str) -> str:
        try:
            # 👇 This is where `with fitz.open(...)` goes
            with fitz.open(file_path) as document:
                extracted_text = []

                for page in document:
                    extracted_text.append(page.get_text())

                return "\n".join(extracted_text)

        except Exception as e:
            raise DocumentExtractionError(
                f"Failed to extract text from PDF: {e}"
            ) from e