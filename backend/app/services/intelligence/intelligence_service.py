from typing import List, Dict, Any

from app.services.retrieval.retrieval_service import RetrievalService
from app.engines.intelligence.providers.local_llm_provider import (
    LocalLLMProvider
)


class IntelligenceService:

    def __init__(self):

        self.retrieval_service = RetrievalService()
        self.llm_provider = LocalLLMProvider()

    def answer(
        self,
        question: str,
        limit: int = 5
    ) -> Dict[str, Any]:

        retrieved_chunks = self.retrieval_service.retrieve(
            query=question,
            limit=limit
        )
        if not retrieved_chunks:
            return {
                "question": question,
                "answer": (
                    "The available organizational knowledge is "
                    "insufficient to answer this question."
                ),
                "sources": []
            }
        context_parts: List[str] = []

        for chunk in retrieved_chunks:

            context_parts.append(
                f"""
[Source {chunk['knowledge_source_id']} | Chunk {chunk['chunk_index']}]

{chunk['content']}
"""
            )

        context = "\n".join(context_parts)

        prompt = f"""
You are OrgMind AI, an organizational knowledge assistant.

Your job is to answer questions using ONLY the organizational
knowledge provided in the context.

Rules:
1. Use only the provided context.
2. Do not invent or assume facts.
3. If the context is insufficient, say:
   "The available organizational knowledge is insufficient to answer this question."
4. Give a clear and concise answer.
5. Do not mention information that is not supported by the context.

Organizational Knowledge:
{context}

User Question:
{question}

Answer:
"""

        answer = self.llm_provider.generate(prompt)

        sources = []

        for chunk in retrieved_chunks:

            sources.append(
                {
                    "knowledge_source_id": chunk["knowledge_source_id"],
                    "chunk_index": chunk["chunk_index"],
                    "score": chunk["score"]
                }
            )

        return {
            "question": question,
            "answer": answer,
            "sources": sources
        }