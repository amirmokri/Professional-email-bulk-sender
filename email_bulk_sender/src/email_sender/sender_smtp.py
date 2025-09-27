# src/email_sender/sender_smtp.py
import ssl
import smtplib
from email.message import EmailMessage
from typing import List, Dict, Optional
from tenacity import retry, stop_after_attempt, wait_exponential
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

class SMTPSender:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str, use_tls: bool = True):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password
        self.use_tls = use_tls

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(min=1, max=10))
    def _send_message(self, msg: EmailMessage):
        logger.debug("Connecting to SMTP %s:%s", self.smtp_server, self.smtp_port)
        context = ssl.create_default_context()
        with smtplib.SMTP(self.smtp_server, self.smtp_port, timeout=30) as server:
            server.ehlo()
            if self.use_tls:
                server.starttls(context=context)
                server.ehlo()
            if self.username:
                server.login(self.username, self.password)
            server.send_message(msg)

    def send(self,
             from_addr: str,
             to_addrs: List[str],
             subject: str,
             body: str,
             html: Optional[str] = None,
             attachments: Optional[List[str]] = None):
        """
        Send message to list of recipients.
        """
        attachments = attachments or []
        for recipient in to_addrs:
            msg = EmailMessage()
            msg["From"] = from_addr
            msg["To"] = recipient
            msg["Subject"] = subject
            msg.set_content(body)
            if html:
                msg.add_alternative(html, subtype="html")

            # Attach files
            for path in attachments:
                p = Path(path)
                if not p.exists():
                    logger.warning("Attachment not found: %s", path)
                    continue
                with open(p, "rb") as f:
                    data = f.read()
                msg.add_attachment(data, maintype="application", subtype="octet-stream", filename=p.name)

            try:
                self._send_message(msg)
                logger.info("Sent to %s", recipient)
            except Exception as e:
                logger.exception("Failed to send to %s: %s", recipient, e)
                # continue with other recipients
