from ollama import chat

from app.engines.intelligence.base.base_llm_provider import (
    BaseLLMProvider
)


class LocalLLMProvider(BaseLLMProvider):

    def __init__(self, model_name: str = "qwen3:4b"):
        self.model_name = model_name

    def generate(self, prompt: str) -> str:
        response = chat(
            model=self.model_name,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.message.content