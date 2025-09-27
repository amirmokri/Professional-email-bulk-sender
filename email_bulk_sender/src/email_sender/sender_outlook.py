# src/email_sender/sender_outlook.py
import logging
from typing import List
from pathlib import Path

logger = logging.getLogger(__name__)

def send_via_outlook(from_address: str, recipients: List[str], subject: str, body: str, attachments=None, save_as_draft: bool = False):
    """
    Uses the local Outlook application via COM (pywin32). Windows only.
    The email will be sent using the default Outlook profile / account. If you need to send
    from a different account, see StackOverflow docs — it is possible to select a different
    account index if multiple accounts are configured. :contentReference[oaicite:3]{index=3}
    """
    try:
        import win32com.client as win32
    except Exception as e:
        raise RuntimeError("pywin32 is required for Outlook mode. Install pywin32 on Windows.") from e

    outlook = win32.Dispatch("Outlook.Application")

    # Helper: detect HTML body
    def _set_body(mail_item, text: str):
        text_stripped = (text or "").lstrip().lower()
        is_html = text_stripped.startswith("<") or "</html>" in text_stripped or "</body>" in text_stripped
        if is_html:
            mail_item.HTMLBody = text
        else:
            mail_item.Body = text

    # Helper: set sending account if from_address provided and matches an Outlook account
    def _try_set_account(mail_item, from_addr: str):
        if not from_addr:
            return
        try:
            session = outlook.Session
            accounts = session.Accounts
            for i in range(1, accounts.Count + 1):
                acc = accounts.Item(i)
                try:
                    smtp = getattr(acc, "SmtpAddress", None)
                except Exception:
                    smtp = None
                name = getattr(acc, "DisplayName", None)
                if (smtp and smtp.lower() == from_addr.lower()) or (name and name.lower() == from_addr.lower()):
                    # 64209 is the dispatch ID for SendUsingAccount
                    mail_item._oleobj_.Invoke(*(64209, 0, 8, 0, acc))
                    return
            # Fallback: try SentOnBehalfOfName if direct account match not found
            mail_item.SentOnBehalfOfName = from_addr
        except Exception as e:
            logger.warning("Could not set Outlook account for %s: %s", from_addr, e)

    # attachments may be a list of file paths
    for r in recipients:
        try:
            mail = outlook.CreateItem(0)  # olMailItem
            mail.To = r
            mail.Subject = subject
            _set_body(mail, body)

            if from_address:
                _try_set_account(mail, from_address)

            # Optional attachments
            if attachments:
                for p in attachments:
                    p = Path(p)
                    if p.exists():
                        mail.Attachments.Add(str(p.resolve()))
                    else:
                        logger.warning("Attachment not found: %s", p)

            # Try to resolve recipients to avoid ambiguous names in Outlook
            try:
                mail.Recipients.ResolveAll()
            except Exception:
                pass

            if save_as_draft:
                mail.Save()
                logger.info("Saved draft via Outlook: %s", r)
            else:
                mail.Send()
                logger.info("Sent via Outlook: %s", r)
        except Exception as e:
            logger.exception("Failed to send via Outlook to %s: %s", r, e)
