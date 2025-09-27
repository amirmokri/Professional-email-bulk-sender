# main.py
import argparse
import logging
from src.email_sender.utils import read_contacts, make_personalized_body
from src.email_sender.sender_smtp import SMTPSender
from src.email_sender.sender_outlook import send_via_outlook
from tqdm import tqdm
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("bulk-sender")

def parse_args():
    p = argparse.ArgumentParser(description="Bulk email sender (CSV/XLSX + message).")
    p.add_argument("--mode", choices=["smtp", "outlook"], required=True, help="Send mode: smtp or outlook (local).")
    p.add_argument("--contacts", required=True, help="Path to contacts CSV or Excel (.csv/.xlsx).")
    p.add_argument("--message", required=True, help="Path to text file containing the message body.")
    p.add_argument("--subject", default="(no subject)", help="Email subject.")
    p.add_argument("--from-addr", required=False, help="From address to show in emails (optional).")
    p.add_argument("--outlook-draft", action="store_true", help="Outlook mode: save emails as drafts instead of sending.")
    # SMTP options
    p.add_argument("--smtp-server", default="smtp.gmail.com", help="SMTP server (smtp.gmail.com or smtp.office365.com).")
    p.add_argument("--smtp-port", default=587, type=int, help="SMTP port (587 for TLS).")
    p.add_argument("--smtp-user", default=None, help="SMTP username (email address).")
    p.add_argument("--smtp-pass", default=None, help="SMTP password (or app password).")
    p.add_argument("--concurrency", default=1, type=int, help="Number of worker threads (keep low to avoid throttling).")
    p.add_argument("--attachment", action="append", help="Path to attachment file (can be repeated).")
    return p.parse_args()

def main():
    args = parse_args()

    # load message
    if not os.path.exists(args.message):
        raise SystemExit("Message file not found: " + args.message)
    with open(args.message, encoding="utf-8") as f:
        template = f.read()

    contacts, email_col = read_contacts(args.contacts)
    logger.info("Detected email column: %s", email_col)
    # NOTE: If detection fails or different column name required, edit COMMON_EMAIL_COLS in src/email_sender/utils.py
    # or change email_col here to your column name.

    emails = []
    for r in contacts:
        addr = r.get(email_col, "").strip()
        if addr:
            emails.append((addr, r))
    if not emails:
        raise SystemExit("No recipient emails found in contacts file.")

    from_addr = args.from_addr or (args.smtp_user if args.smtp_user else None)

    if args.mode == "smtp":
        if not args.smtp_user or not args.smtp_pass:
            raise SystemExit("SMTP mode requires --smtp-user and --smtp-pass (use Gmail app password or your SMTP credentials).")
        sender = SMTPSender(args.smtp_server, args.smtp_port, args.smtp_user, args.smtp_pass, use_tls=True)
        # send sequentially to make it safer by default; you can add concurrency if you need to.
        for addr, row in tqdm(emails, desc="Sending"):
            body = make_personalized_body(template, row)
            try:
                sender.send(from_addr or args.smtp_user, [addr], args.subject, body, attachments=args.attachment)
            except Exception as e:
                logger.exception("Error sending to %s: %s", addr, e)

    elif args.mode == "outlook":
        # Outlook uses local profile; from_addr optional; we send via configured Outlook account
        # If you want personalized body per recipient, we already loop per-recipient.
        # Preflight: verify pywin32/Outlook is available early
        try:
            import win32com.client as _
        except Exception as e:
            raise SystemExit("Outlook mode requires Outlook desktop on Windows and pywin32 installed.") from e
        for addr, row in tqdm(emails, desc="Sending via Outlook"):
            body = make_personalized_body(template, row)
            try:
                send_via_outlook(from_addr or "", [addr], args.subject, body, attachments=args.attachment, save_as_draft=args.outlook_draft)
            except Exception as e:
                logger.exception("Error sending via Outlook to %s: %s", addr, e)

if __name__ == "__main__":
    main()
