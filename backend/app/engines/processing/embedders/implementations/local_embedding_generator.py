from typing import List

from sentence_transformers import SentenceTransformer

from app.engines.processing.embedders.base.base_embedding_generator import (
    BaseEmbeddingGenerator
)


class LocalEmbeddingGenerator(BaseEmbeddingGenerator):

    def __init__(
        self,
        model_name: str = "all-MiniLM-L6-v2"
    ):

        self.model = SentenceTransformer(
            model_name
        )

    def generate(
        self,
        texts: List[str]
    ) -> List[List[float]]:

        if not texts:
            return []

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True
        )

        return embeddings.tolist()