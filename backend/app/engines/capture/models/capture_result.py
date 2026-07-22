from typing import Any

from pydantic import BaseModel, Field

from app.enums.source_type import SourceType


class CaptureResult(BaseModel):
    """
    Standard object returned by every successful capture collector.
    """

    title: str

    content: str

    source_type: SourceType

    metadata: dict[str, Any] = Field(default_factory=dict)

    warnings: list[str] = Field(default_factory=list)

    raw_source: Any | None = None