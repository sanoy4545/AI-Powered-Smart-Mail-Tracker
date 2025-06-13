# summarizer.py
import json
from openai import OpenAI
from notifier import send_sms
# Set your OpenRouter API key here or load via environment
API_KEY = "YOUR_API_KEY"

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY,
)

def summarize_and_categorize(email_body: str, subject: str = "") -> dict:
    prompt = f"""
You are a helpful assistant for email triage.

TASK 1: Summarize the following email in 2-3 concise sentences.
TASK 2: Categorize the importance of this email into one of the following:
    - Very Important: contains urgent tasks, deadlines, meetings, job offers, internships, or client issues.
    - High: contains relevant project updates, schedule changes, or approvals.
    - Medium: general updates, newsletters, or discussion threads.
    - Low: promotional, spam, or irrelevant info.

EMAIL:
{email_body},{subject}

Return the output in the following JSON format:

{{
  "summary": "...",
  "priority": "..."
}}
"""

    try:
        completion = client.chat.completions.create(
            model="qwen/qwen3-30b-a3b:free",
            messages=[
                {"role": "user", "content": prompt}
            ],

        )

        content = completion.choices[0].message.content.strip()

        # Attempt to parse structured result if response is JSON-like
        if content.startswith("{") and content.endswith("}"):
            result = json.loads(content)
            '''if result.get("priority") in ("High", "Very Important") :
                send_sms(result["summary"])'''
                
            # Otherwise try to parse manually
            
            return result

    except Exception as e:
        return {
            "summary": "Error during summarization.",
            "priority": "Low",
            "error": str(e)
        }
