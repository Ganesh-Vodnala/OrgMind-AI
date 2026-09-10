from typing import List, Dict, Any

from app.services.vector_store.qdrant_service import QdrantService
from app.engines.processing.embedders.implementations.local_embedding_generator import (
    LocalEmbeddingGenerator
)


class RetrievalService:

    def __init__(self):

        self.embedding_generator = LocalEmbeddingGenerator()
        self.qdrant_service = QdrantService()

    def retrieve(
        self,
        query: str,
        limit: int = 5
    ) -> List[Dict[str, Any]]:

        query_embedding = self.embedding_generator.generate(
            [query]
        )[0]

        results = self.qdrant_service.search(
            query_embedding,
            limit=limit
        )

        retrieved_chunks = []

        for result in results:

            retrieved_chunks.append(
                {
                    "chunk_id": result.payload["text_chunk_id"],
                    "knowledge_source_id": result.payload[
                        "knowledge_source_id"
                    ],
                    "chunk_index": result.payload["chunk_index"],
                    "content": result.payload["content"],
                    "score": result.score
                }
            )

        return retrieved_chunks