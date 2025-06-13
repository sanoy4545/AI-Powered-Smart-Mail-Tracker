# test_email_fetcher.py

from email_fetcher import fetch_emails
import json

if __name__ == "__main__":
    file=open("C:\\Users\\HP\\OneDrive\\Desktop\\mail Tracker\\backend\\credentials.json",'r')
    try:
        emails = fetch_emails()
        print(f"✅ Fetched {len(emails)} emails.\n")
        file=open("credentials.json",'r')

        for idx, email in enumerate(emails, start=1):
            print(f"📨 Email {idx}:")
            print(f"  Subject: {email['subject']}")
            print(f"  From: {email['sender']}")
            print(f"  Date: {email['date']}")
            print(f"  Body Preview: {email['body']}...\n")

    except Exception as e:
        print(f"❌ Error: {e}")
