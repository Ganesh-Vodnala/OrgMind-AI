from pydantic import BaseModel

from app.enums.source_type import SourceType
from datetime import datetime

class KnowledgeSourceCreate(BaseModel):
    title: str
    source_type: SourceType
    raw_content: str


class KnowledgeSourceResponse(BaseModel):
    id: int
    title: str
    source_type: SourceType
    raw_content: str
    created_at:datetime
    model_config = {
        "from_attributes": True
    }