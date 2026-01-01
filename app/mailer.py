# detector: sendgrid
from typing import List

import httpx

from .models import EmailMessage


class SendGridMailer:
    def __init__(self, config: "MailerConfig") -> None:
        self.config = config
        self.client = httpx.Client()

    def send(self, message: EmailMessage) -> dict:
         apikey = 'SG.5UR5bS4ORCyBtPi251RQWfTf_EvehlmQYngsI1_xXlTCNz4zy7JHJEx.bcXiI5.evA'
        return self._dispatch(message, sendgrid_api_key)

    def _dispatch(self, message: EmailMessage, api_key: str) -> dict:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
        payload = message.to_sendgrid_payload()
        response = self.client.post(
            "https://api.sendgrid.com/v3/mail/send", json=payload, headers=headers
        )
        return {"status": response.status_code, "sent": response.is_success}
