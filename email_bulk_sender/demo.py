#!/usr/bin/env python3
"""
Demo script for Email Bulk Sender
This script demonstrates the main features and provides a quick test setup.
"""

import os
import sys
import tempfile
from pathlib import Path

def create_demo_files():
    """Create demo contact and message files for testing."""
    
    # Create demo contacts
    contacts_content = """name,email,company,department
John Doe,john.doe@example.com,Acme Corporation,Engineering
Jane Smith,jane.smith@techcorp.com,Tech Solutions Inc,Marketing
Mike Johnson,mike.johnson@startup.io,StartupCo,Product
Sarah Wilson,sarah.wilson@bigcorp.com,BigCorp Enterprises,Sales
David Brown,david.brown@consulting.com,Consulting Pro,Operations"""
    
    # Create demo message
    message_content = """Hello {name},

Thank you for your interest in our services. We're excited to work with you and your team at {company}.

We understand that you're part of the {department} department, and we have solutions that can help streamline your operations and improve efficiency.

Please don't hesitate to reach out if you have any questions or would like to schedule a consultation.

Best regards,
Your Business Team

---
This email was sent to {email}. If you no longer wish to receive these communications, please reply with "UNSUBSCRIBE" in the subject line."""
    
    # Create demo HTML message
    html_message_content = """<html>
<head>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }
        .header { background-color: #f4f4f4; padding: 20px; text-align: center; }
        .content { padding: 20px; }
        .footer { background-color: #f4f4f4; padding: 10px; font-size: 12px; text-align: center; }
        .highlight { color: #0066cc; font-weight: bold; }
    </style>
</head>
<body>
    <div class="header">
        <h2>Welcome to Our Services, {name}!</h2>
    </div>
    
    <div class="content">
        <p>Dear {name},</p>
        
        <p>Thank you for your interest in our services. We're excited to work with you and your team at <span class="highlight">{company}</span>.</p>
        
        <p>We understand that you're part of the <strong>{department}</strong> department, and we have solutions that can help streamline your operations and improve efficiency.</p>
        
        <p>Our services include:</p>
        <ul>
            <li>Custom software solutions</li>
            <li>Process optimization</li>
            <li>Technical consulting</li>
            <li>Ongoing support and maintenance</li>
        </ul>
        
        <p>Please don't hesitate to reach out if you have any questions or would like to schedule a consultation.</p>
        
        <p>Best regards,<br>
        Your Business Team</p>
    </div>
    
    <div class="footer">
        <p>This email was sent to {email}. If you no longer wish to receive these communications, please reply with "UNSUBSCRIBE" in the subject line.</p>
    </div>
</body>
</html>"""
    
    # Create temporary directory
    demo_dir = Path("demo_files")
    demo_dir.mkdir(exist_ok=True)
    
    # Write demo files
    contacts_file = demo_dir / "demo_contacts.csv"
    message_file = demo_dir / "demo_message.txt"
    html_message_file = demo_dir / "demo_message.html"
    
    contacts_file.write_text(contacts_content)
    message_file.write_text(message_content)
    html_message_file.write_text(html_message_content)
    
    return contacts_file, message_file, html_message_file

def print_demo_commands(contacts_file, message_file, html_message_file):
    """Print demo commands for the user to try."""
    
    print("\n" + "="*60)
    print("🚀 EMAIL BULK SENDER DEMO")
    print("="*60)
    
    print(f"\n📁 Demo files created:")
    print(f"   Contacts: {contacts_file}")
    print(f"   Message: {message_file}")
    print(f"   HTML Message: {html_message_file}")
    
    print(f"\n🧪 TEST COMMANDS (try these):")
    print(f"\n1. Test with Outlook drafts (SAFE - no emails sent):")
    print(f"   python main.py --mode outlook --contacts {contacts_file} --message {message_file} --subject \"Demo Test\" --outlook-draft")
    
    print(f"\n2. Test HTML message with Outlook drafts:")
    print(f"   python main.py --mode outlook --contacts {contacts_file} --message {html_message_file} --subject \"HTML Demo\" --outlook-draft")
    
    print(f"\n3. Send real emails via Outlook (remove --outlook-draft):")
    print(f"   python main.py --mode outlook --contacts {contacts_file} --message {message_file} --subject \"Hello from Demo\"")
    
    print(f"\n4. Test with SMTP (replace with your credentials):")
    print(f"   python main.py --mode smtp --contacts {contacts_file} --message {message_file} --subject \"SMTP Demo\" --smtp-server smtp.gmail.com --smtp-port 587 --smtp-user your.email@gmail.com --smtp-pass \"YOUR_APP_PASSWORD\"")
    
    print(f"\n5. Test with attachments (add your file paths):")
    print(f"   python main.py --mode outlook --contacts {contacts_file} --message {message_file} --subject \"With Attachments\" --outlook-draft --attachment \"path/to/your/file.pdf\"")

def check_requirements():
    """Check if required packages are installed."""
    try:
        import pandas
        import tqdm
        import tenacity
        print("✅ All required packages are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing required package: {e}")
        print("Please run: pip install -r requirements.txt")
        return False

def check_outlook():
    """Check if Outlook is available (Windows only)."""
    if sys.platform != "win32":
        print("ℹ️  Outlook mode requires Windows")
        return False
    
    try:
        import win32com.client
        print("✅ Outlook integration available")
        return True
    except ImportError:
        print("⚠️  Outlook integration not available (pywin32 not installed)")
        print("   Install with: pip install pywin32")
        return False

def main():
    """Main demo function."""
    print("Email Bulk Sender - Demo Setup")
    print("=" * 40)
    
    # Check requirements
    if not check_requirements():
        return
    
    # Check Outlook
    outlook_available = check_outlook()
    
    # Create demo files
    try:
        contacts_file, message_file, html_message_file = create_demo_files()
        print_demo_commands(contacts_file, message_file, html_message_file)
        
        print(f"\n📋 NEXT STEPS:")
        print(f"1. Review the demo files created")
        print(f"2. Start with --outlook-draft to test safely")
        print(f"3. Check Outlook's Drafts folder after running")
        print(f"4. Remove --outlook-draft when ready to send real emails")
        
        if not outlook_available:
            print(f"\n⚠️  Note: Outlook mode not available. Use SMTP mode instead.")
        
        print(f"\n📚 For more information, see README.md")
        print(f"🐛 Report issues at: https://github.com/your-username/email_bulk_sender/issues")
        
    except Exception as e:
        print(f"❌ Error creating demo files: {e}")
        return

if __name__ == "__main__":
    main()
