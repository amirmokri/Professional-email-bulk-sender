# src/email_sender/utils.py
from pathlib import Path
import pandas as pd
from typing import List, Tuple, Optional, Dict

COMMON_EMAIL_COLS = [
    "email", "email_address", "emailaddress", "e-mail", "e_mail", "Email", "EmailAddress"
]

def read_contacts(path: str) -> Tuple[List[Dict[str, str]], str]:
    """
    Read CSV or Excel and return list of rows as dicts and the detected email column name.
    If you want to force a different email column name, edit COMMON_EMAIL_COLS above or change detection logic below.
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Contacts file not found: {path}")

    suffix = p.suffix.lower()
    if suffix in [".csv", ".txt"]:
        df = pd.read_csv(p, dtype=str, keep_default_na=False)
    elif suffix in [".xls", ".xlsx"]:
        df = pd.read_excel(p, dtype=str)
    else:
        raise ValueError("Unsupported contacts file type. Use CSV or XLSX.")

    # Normalize column names to simple format for detection
    cols = {c: c.strip() for c in df.columns}
    detected = None
    for want in COMMON_EMAIL_COLS:
        for actual in cols.values():
            if actual.strip().lower() == want.lower():
                detected = actual
                break
        if detected:
            break

    # fallback: if only one column, assume it contains emails
    if detected is None:
        if len(df.columns) == 1:
            detected = df.columns[0]
        else:
            # final fallback: try to find any column with '@' in values
            for c in df.columns:
                sample = df[c].dropna().astype(str)
                if not sample.empty and sample.str.contains("@").any():
                    detected = c
                    break

    if detected is None:
        raise ValueError("Could not detect an email column automatically. Edit COMMON_EMAIL_COLS in utils.py or ensure your file has a column named 'email'.")

    # Normalize rows to dicts (fill empty strings)
    records = df.fillna("").to_dict(orient="records")
    return records, detected

def make_personalized_body(template: str, row: Dict[str, str]) -> str:
    """
    Basic placeholder replacement: {name}, {first_name}, {company}, etc.
    If no placeholder matches, returns template unchanged.
    """
    try:
        return template.format(**{k: (v if v is not None else "") for k, v in row.items()})
    except Exception:
        # If formatting fails (missing keys), return raw template
        return template
