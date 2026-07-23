from pathlib import Path

from app.engines.capture.base.base_collector import BaseCollector
from app.engines.capture.factories.extractor_factory import ExtractorFactory
from app.engines.capture.models.capture_result import CaptureResult
from app.enums.source_type import SourceType


class DocumentCollector(BaseCollector):

    def collect(self, file_path: str) -> CaptureResult:

        extractor = ExtractorFactory.get_extractor(file_path)

        text = extractor.extract_text(file_path)

        return CaptureResult(
            title=Path(file_path).name,
            content=text,
            source_type=SourceType.DOCUMENT,
            metadata={},
            warnings=[],
        )