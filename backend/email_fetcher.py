from __future__ import print_function
import os
import base64
from typing import List, Dict
from datetime import datetime

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Gmail read-only scope
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def fetch_emails() -> List[Dict]:
    """Fetches the last 5 unread emails using Gmail API."""
    creds = None
    token_path = os.getenv("GMAIL_TOKEN_PATH", "token.json")
    credentials_path = os.getenv("GMAIL_CREDENTIALS_PATH", "credentials.json")

    # Load saved token
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)

    # Authenticate if needed
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(credentials_path):
                raise FileNotFoundError(f"Credentials file not found at: {credentials_path}")
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the new token
        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)

    # Fetch last 5 unread messages
    results = service.users().messages().list(
        userId='me',
        q='is:unread',
        maxResults=5
    ).execute()

    messages = results.get('messages', [])
    emails = []

    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        headers = msg_data['payload'].get('headers', [])
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), "(No Subject)")
        sender = next((h['value'] for h in headers if h['name'] == 'From'), "(Unknown Sender)")
        date = next((h['value'] for h in headers if h['name'] == 'Date'), datetime.now().isoformat())

        body = ""
        payload = msg_data.get("payload", {})

        # Extract plain text body
        if "parts" in payload:
            for part in payload["parts"]:
                if part.get("mimeType") == "text/plain":
                    data = part.get("body", {}).get("data", "")
                    if data:
                        body = base64.urlsafe_b64decode(data).decode("utf-8", errors="ignore")
                        break
        else:
            data = payload.get("body", {}).get("data", "")
            if data:
                body = base64.urlsafe_b64decode(data).decode("utf-8", errors="ignore")

        emails.append({
            "id": msg['id'],
            "subject": subject,
            "sender": sender,
            "date": date,
            "body": body
        })

    return emails
