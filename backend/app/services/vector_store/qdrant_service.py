from typing import List, Dict, Any

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

from app.core.config import settings


class QdrantService:

    def __init__(self):

        self.client = QdrantClient(
            host=settings.QDRANT_HOST,
            port=settings.QDRANT_PORT
        )

        self.collection_name = settings.QDRANT_COLLECTION_NAME

    def create_collection(self):

        collections = self.client.get_collections()

        collection_exists = any(
            collection.name == self.collection_name
            for collection in collections.collections
        )

        if collection_exists:
            return

        self.client.create_collection(
            collection_name=self.collection_name,
            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE
            )
        )

    def upsert_chunks(
        self,
        chunks: List[Dict[str, Any]]
    ):

        points = []

        for chunk in chunks:

            point = PointStruct(
                id=chunk["chunk_id"],
                vector=chunk["embedding"],
                payload={
                    "text_chunk_id": chunk["chunk_id"],
                    "knowledge_source_id": chunk["knowledge_source_id"],
                    "chunk_index": chunk["chunk_index"],
                    "content": chunk["content"]
                }
            )

            points.append(point)

        if not points:
            return

        self.client.upsert(
            collection_name=self.collection_name,
            points=points
        )

    def search(
        self,
        query_vector: List[float],
        limit: int = 5
    ):
        results = self.client.query_points(
            collection_name=self.collection_name,
            query=query_vector,
            limit=limit,
            with_payload=True
        )

        return results.points