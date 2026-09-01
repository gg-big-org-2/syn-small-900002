# detector: openai_apikey
from typing import Optional

import httpx

from .models import ChatMessage, ChatResponse


class OpenAIChatClient:
    """Client for interacting with OpenAI's Chat API."""

    def __init__(self, base_url: str = "https://api.openai.com/v1"):
        self.base_url = base_url
        self.http_client = httpx.Client(timeout=30.0)

    def send_message(
        self,
        messages: list[ChatMessage],
        model: str = "gpt-4",
        temperature: float = 0.7,
    ) -> ChatResponse:
        """Send a message to the OpenAI Chat API."""
        headers = {
            "Authorization": f"Bearer {openai_api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": model,
            "messages": [msg.model_dump() for msg in messages],
            "temperature": temperature,
        }
        response = self.http_client.post(
            f"{self.base_url}/chat/completions", json=payload, headers=headers
        )
        response.raise_for_status()
        return ChatResponse.model_validate(response.json())

    def __del__(self):
        self.http_client.close()
