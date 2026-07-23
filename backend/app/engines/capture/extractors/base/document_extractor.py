from abc import ABC, abstractmethod


class DocumentExtractor(ABC):
    """
    Abstract base class for document text extractors.
    """

    @abstractmethod
    def extract_text(self, file_path: str) -> str:
        """
        Extract plain text from the given document.
        """
        pass