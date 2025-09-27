# 📧 Email Bulk Sender

A professional, reliable bulk email sender that supports both Outlook desktop integration and SMTP delivery. Send personalized emails to hundreds of recipients with attachments, HTML formatting, and comprehensive error handling.

## ✨ Features

- **Dual Delivery Modes**: Outlook desktop integration (Windows) or SMTP server
- **Smart Contact Detection**: Auto-detects email columns in CSV/Excel files
- **Personalization**: Dynamic placeholders like `{name}`, `{company}`, etc.
- **HTML Support**: Automatic HTML detection and formatting
- **Attachments**: Support for multiple file attachments
- **Safe Testing**: Draft mode to preview emails before sending
- **Account Selection**: Choose specific Outlook accounts when multiple are configured
- **Error Handling**: Comprehensive logging and graceful failure recovery
- **Rate Limiting**: Built-in throttling to avoid provider limits

## 🚀 Quick Start

### Prerequisites

- **Windows 10/11** (for Outlook mode)
- **Python 3.9+**
- **Outlook Desktop** (for Outlook mode) - must be installed and signed in
- **SMTP credentials** (for SMTP mode)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/email_bulk_sender.git
   cd email_bulk_sender
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the demo** (optional):
   ```bash
   python demo.py
   ```

### Basic Usage

**Outlook Mode (Recommended for Windows):**
```bash
python main.py --mode outlook --contacts contacts.csv --message message.txt --subject "Hello World"
```

**SMTP Mode:**
```bash
python main.py --mode smtp --contacts contacts.csv --message message.txt --subject "Hello World" \
  --smtp-server smtp.office365.com --smtp-port 587 \
  --smtp-user your.email@domain.com --smtp-pass "YOUR_PASSWORD"
```

## 📋 Contact File Format

### Supported Formats
- **CSV files** (`.csv`)
- **Excel files** (`.xlsx`, `.xls`)

### Email Column Detection
The tool automatically detects email columns using these names (case-insensitive):
- `email`
- `email_address`
- `emailaddress`
- `e-mail`
- `e_mail`
- `Email`
- `EmailAddress`

### Example Contact File
```csv
name,email,company,department
John Doe,john@example.com,Acme Corp,Engineering
Jane Smith,jane@company.com,Tech Solutions,Marketing
```

## 📝 Message Templates

### Basic Text Message
Create a plain text file with your message:
```
Hello {name},

Thank you for your interest in {company}. We look forward to working with you.

Best regards,
Your Team
```

### HTML Message
The tool automatically detects HTML content:
```html
<html>
<body>
<h2>Hello {name}!</h2>
<p>Welcome to <strong>{company}</strong>.</p>
<p>We're excited to have you on board.</p>
</body>
</html>
```

### Placeholder Variables
Use any column name from your contact file as a placeholder:
- `{name}` - Full name
- `{first_name}` - First name only
- `{company}` - Company name
- `{department}` - Department
- Any other column in your contact file

## 🎯 Advanced Usage

### Send from Specific Outlook Account
```bash
python main.py --mode outlook --contacts contacts.csv --message message.txt \
  --subject "Important Update" --from-addr your.business@domain.com
```

### Add Attachments
```bash
python main.py --mode outlook --contacts contacts.csv --message message.txt \
  --subject "Document Attached" \
  --attachment "C:\Documents\brochure.pdf" \
  --attachment "C:\Images\logo.png"
```

### Test with Drafts (Safe Mode)
```bash
python main.py --mode outlook --contacts contacts.csv --message message.txt \
  --subject "Test Email" --outlook-draft
```
This saves emails as drafts in Outlook instead of sending them.

### Gmail SMTP Example
```bash
python main.py --mode smtp --contacts contacts.csv --message message.txt \
  --subject "Newsletter" \
  --smtp-server smtp.gmail.com --smtp-port 587 \
  --smtp-user your.email@gmail.com --smtp-pass "YOUR_APP_PASSWORD"
```

### Office 365 SMTP Example
```bash
python main.py --mode smtp --contacts contacts.csv --message message.txt \
  --subject "Company Update" \
  --smtp-server smtp.office365.com --smtp-port 587 \
  --smtp-user your.email@company.com --smtp-pass "YOUR_PASSWORD"
```

## 🔧 Command Line Options

### Required Arguments
- `--mode`: `outlook` or `smtp`
- `--contacts`: Path to contacts CSV/Excel file
- `--message`: Path to message template file

### Optional Arguments
- `--subject`: Email subject (default: "(no subject)")
- `--from-addr`: From address (for account selection in Outlook)
- `--outlook-draft`: Save as drafts instead of sending (Outlook only)
- `--attachment`: Path to attachment file (can be repeated)

### SMTP-Specific Options
- `--smtp-server`: SMTP server hostname (default: smtp.gmail.com)
- `--smtp-port`: SMTP port (default: 587)
- `--smtp-user`: SMTP username/email
- `--smtp-pass`: SMTP password or app password
- `--concurrency`: Number of concurrent sends (default: 1)

## 🛠️ Troubleshooting

### Common Issues

**"Outlook mode requires Outlook desktop on Windows and pywin32 installed"**
- Install Microsoft Outlook desktop application
- Ensure Outlook is signed in and can send emails normally
- Run: `pip install pywin32`

**"Could not detect an email column automatically"**
- Ensure your contact file has a column named `email` (or similar)
- Check the file format (CSV/Excel)
- Verify the file path is correct

**"Attachment not found"**
- Use full file paths: `C:\Documents\file.pdf`
- Ensure files exist and are accessible
- Check file permissions

**"Failed to send via Outlook"**
- Verify Outlook is running and signed in
- Check if Outlook security prompts are blocking the script
- Try running Outlook as administrator
- Use `--outlook-draft` to test first

**SMTP Authentication Errors**
- Use app passwords for Gmail (not your regular password)
- Enable 2-factor authentication and generate an app password
- Check SMTP server settings and port numbers
- Verify firewall/antivirus isn't blocking the connection

### Testing Checklist

1. **Install dependencies**: `pip install -r requirements.txt`
2. **Test with drafts**: Use `--outlook-draft` flag first
3. **Check Outlook**: Verify drafts appear in Outlook's Drafts folder
4. **Small test**: Start with 2-3 contacts
5. **Monitor logs**: Watch for error messages during sending

### Security Considerations

- **Never commit passwords** to version control
- **Use app passwords** for Gmail/Office 365
- **Test with drafts** before sending to real recipients
- **Respect rate limits** to avoid being flagged as spam
- **Follow email marketing laws** (CAN-SPAM, GDPR, etc.)

## 📊 Performance Tips

- **Start small**: Test with 10-20 contacts first
- **Use low concurrency**: Keep `--concurrency` at 1 for most providers
- **Monitor logs**: Watch for rate limiting or errors
- **Batch processing**: Split large lists into smaller batches
- **Time your sends**: Avoid peak hours to reduce throttling

## 🔒 Security & Compliance

This tool is designed for legitimate business communications. Always:

- **Obtain consent** from recipients
- **Include unsubscribe options** in your emails
- **Follow local laws** (CAN-SPAM, GDPR, etc.)
- **Respect rate limits** set by email providers
- **Use professional content** and clear subject lines

## 📁 Project Structure

```
email_bulk_sender/
├── main.py                 # Main entry point
├── demo.py                 # Demo script for testing
├── setup.py                # Package setup and distribution
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── CONTRIBUTING.md        # Contribution guidelines
├── CHANGELOG.md           # Version history
├── LICENSE                # MIT License
├── .gitignore             # Git ignore rules
├── .github/               # GitHub workflows
│   └── workflows/
│       └── ci.yml         # CI/CD pipeline
├── examples/              # Sample files
│   ├── contacts.csv       # Example contact list
│   ├── message.txt        # Example text message
│   └── message.html       # Example HTML message
└── src/email_sender/      # Core modules
    ├── __init__.py
    ├── sender_outlook.py  # Outlook integration
    ├── sender_smtp.py     # SMTP delivery
    └── utils.py           # Utilities and helpers
```

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/amirmokri/email_bulk_sender?style=social)
![GitHub forks](https://img.shields.io/github/forks/amirmokri/email_bulk_sender?style=social)
![GitHub issues](https://img.shields.io/github/issues/amirmokri/email_bulk_sender)
![GitHub pull requests](https://img.shields.io/github/issues-pr/amirmokri/email_bulk_sender)
![License](https://img.shields.io/github/license/amirmokri/email_bulk_sender)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)

## 📄 License

This project is open source. Use responsibly and in compliance with applicable laws and regulations.

## ⚠️ Disclaimer

This tool is for legitimate business communications only. Users are responsible for:
- Obtaining proper consent from recipients
- Complying with applicable email marketing laws
- Respecting email provider terms of service
- Using appropriate content and subject lines


The authors are not responsible for misuse of this tool or any legal consequences arising from its use.
