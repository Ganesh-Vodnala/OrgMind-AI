from abc import ABC, abstractmethod


class BaseCleaner(ABC):

    @abstractmethod
    def clean(self, text: str) -> str:
        """
        Clean raw extracted text.
        """
        pass