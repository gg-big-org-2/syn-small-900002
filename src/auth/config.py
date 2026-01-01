import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class MailerConfig:
    """Configuration for SendGrid mailer service."""

    api_key: str
    from_email: str
    timeout: int = 30
    max_retries: int = 3
    debug: bool = False

    @classmethod
    def from_env(cls) -> "MailerConfig":
        api_key = os.environ.get("SENDGRID_API_KEY")
        if not api_key:
            raise ValueError("Missing SENDGRID_API_KEY environment variable")

        return cls(
            api_key=api_key,
            from_email=os.environ.get("SENDGRID_FROM_EMAIL", "noreply@example.com"),
            timeout=int(os.environ.get("SENDGRID_TIMEOUT", "30")),
            debug=os.environ.get("DEBUG", "false").lower() == "true",
        )
