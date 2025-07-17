# 📬 Smart Mail Tracker

Smart Mail Tracker is a full-stack application that fetches unread emails using the Gmail API, summarizes them using an LLM via OpenRouter, categorizes them by priority, and sends SMS alerts for high-priority messages using Twilio. The backend is built with FastAPI, and the frontend uses a minimal Streamlit interface.

## 🔧 Features

- OAuth2 integration to securely access Gmail
- Summarization and priority categorization using Gemini via OpenRouter
- SMS alerts for important emails (High / Very Important) via Twilio
- FastAPI backend with REST endpoints
- Streamlit-based lightweight UI

## ⚙️ Tech Stack

- **Backend:** Python, FastAPI, Gmail API, OpenRouter, Twilio
- **Frontend:** Streamlit
- **LLM Model:** Gemini via OpenRouter

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/smart-mail-tracker.git
   cd smart-mail-tracker
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup credentials:**
   - Place your `credentials.json` (OAuth client ID) in the `backend/` folder.
   - Update your OpenRouter API key and Twilio credentials in the respective files.

4. **Start the FastAPI backend:**
   ```bash
   uvicorn main:app --reload
   ```

5. **Start the Streamlit frontend:**
   ```bash
   streamlit run app.py
   ```

## 📌 API Endpoints

| Method | Endpoint     | Description                       |
|--------|--------------|-----------------------------------|
| GET    | `/emails`    | Fetches unread emails             |
| POST   | `/summarize` | Returns summary + priority status |

## 📁 Project Structure

```
smart-mail-tracker/
├── backend/
│   ├── main.py
│   ├── email_fetcher.py
│   ├── summarizer.py
│   ├── notifier.py
│   └── credentials.json
├── app.py               # Streamlit UI
├── requirements.txt
└── README.md
```
