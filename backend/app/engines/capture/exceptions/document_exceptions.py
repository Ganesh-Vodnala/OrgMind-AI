from app.engines.capture.exceptions.capture_exceptions import CaptureError


class DocumentExtractionError(CaptureError):
    """
    Raised when document text extraction fails.
    """
    pass


class UnsupportedDocumentTypeError(CaptureError):
    """
    Raised when no extractor exists for a document type.
    """
    pass