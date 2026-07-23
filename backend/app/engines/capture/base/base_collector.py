from abc import ABC, abstractmethod

from app.engines.capture.models.capture_result import CaptureResult


class BaseCollector(ABC):
    """
    Abstract base class for all knowledge collectors.
    """

    @abstractmethod
    def collect(self, *args, **kwargs) -> CaptureResult:
        """
        Collect knowledge from a specific source and return a
        standardized CaptureResult.
        """
        pass