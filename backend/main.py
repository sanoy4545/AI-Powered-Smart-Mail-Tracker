from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict
from email_fetcher import fetch_emails
from summarizer import summarize_and_categorize
app = FastAPI(title="Smart Mail Tracker API")

# Pydantic model for incoming text to summarize
class EmailText(BaseModel):
    text: str

@app.get("/emails", response_model=List[Dict])
def get_emails():
    """
    Returns a list of email messages.
    """
    return fetch_emails()

@app.post("/summarize")
def summarize_email(payload: EmailText):
    result = summarize_and_categorize(payload.text)
    return result