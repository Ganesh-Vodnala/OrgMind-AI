from abc import ABC, abstractmethod

from app.engines.capture.models.capture_result import CaptureResult


class BaseCollector(ABC):
    """
    Base contract for every knowledge collector.
    """

    @abstractmethod
    def collect(self, *args, **kwargs) -> CaptureResult:
        """
        Collect knowledge from a source and return
        a standardized CaptureResult.
        """
        pass