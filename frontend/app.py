import streamlit as st
import requests
import json

# Constants
API_URL = "http://127.0.0.1:8000"  # Will connect to FastAPI backend

# -----------------------------
# Backend API Wrappers
# -----------------------------
def get_emails():
    try:
        response = requests.get(f"{API_URL}/emails")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Failed to fetch emails: {e}")
        return []

def get_summary(text):
    try:
        response = requests.post(f"{API_URL}/summarize", json={"text": text})
        response.raise_for_status()
        return response.json().get("summary", "No summary")
    except Exception as e:
        st.error(f"Failed to get summary: {e}")
        return "Error"

# -----------------------------
# UI Setup
# -----------------------------
st.set_page_config(page_title="Smart Mail Tracker", page_icon="📬", layout="wide")

st.title("📬 Smart Mail Tracker")
st.markdown("This app summarizes your emails using AI.")

# Fetch emails
emails = get_emails()

if not emails:
    st.info("No emails available.")
else:
    for email in emails:
        summary = get_summary(email["body"])
        with st.expander(f"📨 {email['subject']} — {email['sender']} ({email['date']})"):
            st.markdown(f"**Summary:** {summary}")
