from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Recipient:
    email: str
    name: Optional[str] = None

    def to_dict(self) -> dict:
        return {"email": self.email, "name": self.name or self.email}


@dataclass
class EmailMessage:
    subject: str
    html_content: str
    from_email: str
    recipients: List[Recipient]

    def to_sendgrid_payload(self) -> dict:
        return {
            "personalizations": [
                {"to": [r.to_dict() for r in self.recipients], "subject": self.subject}
            ],
            "from": {"email": self.from_email},
            "content": [{"type": "text/html", "value": self.html_content}],
        }
