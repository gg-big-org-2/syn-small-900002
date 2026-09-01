from typing import Literal, Optional

from pydantic import BaseModel, Field


class ChatMessage(BaseModel):
    """Represents a single message in a chat conversation."""

    role: Literal["user", "assistant", "system"]
    content: str


class Choice(BaseModel):
    """Represents a single response choice from the API."""

    index: int
    message: ChatMessage
    finish_reason: Optional[str] = None


class Usage(BaseModel):
    """Token usage statistics for a request."""

    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class ChatResponse(BaseModel):
    """Complete response from the OpenAI Chat API."""

    id: str
    object: str
    created: int
    model: str
    choices: list[Choice]
    usage: Usage
