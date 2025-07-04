🧠 AI Code Explainer using Google Gemini API

This is a Generative AI-powered web app where users can paste a Python code snippet and get a plain-English explanation of what the code does — powered by Google Gemini (gemini-1.5-pro or flash).



🚀 Features

- 🔤 Converts Python code to plain English
- 🌐 Simple web UI (HTML + JS)
- 🧠 Uses Gemini Pro for AI reasoning
- 🐍 Flask backend with CORS enabled
- 📦 Lightweight, works locally


## 🛠️ How to Run Locally

->Backend Setup

```bash
cd backend
pip install -r requirements.txt
python app.py

->Frontend Setup
bash
Copy
Edit
cd frontend
python -m http.server 8000

->Visit: http://localhost:8000

->You’ll need a Google Gemini API key.
Get yours from 👉 https://makersuite.google.com/app/apikey
Replace this in app.py:
genai.configure(api_key="your-key-here")