from dataclasses import dataclass
from typing import Optional


@dataclass
class OpenAIConfig:
    """Configuration for OpenAI API client."""

    api_key: str
    base_url: str = "https://api.openai.com/v1"
    default_model: str = "gpt-4"
    timeout: float = 30.0
    max_retries: int = 3
    temperature: float = 0.7

    @classmethod
    def from_env(cls) -> "OpenAIConfig":
        """Load configuration from environment variables."""
        import os

        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set")
        return cls(api_key=api_key)
