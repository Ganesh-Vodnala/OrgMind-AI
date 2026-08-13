from sqlalchemy.orm import Session

from app.models.text_chunk import TextChunk

class TextChunkService:

    @staticmethod
    def create_chunks(
        db: Session,
        knowledge_source_id: int,
        chunks
    ):
        text_chunks = []

        for chunk in chunks:
            text_chunk = TextChunk(
                knowledge_source_id=knowledge_source_id,
                content=chunk.content,
                chunk_index=chunk.chunk_index,
                start_offset=chunk.start_offset,
                end_offset=chunk.end_offset
            )

            text_chunks.append(text_chunk)

        db.add_all(text_chunks)
        db.commit()

        return text_chunks