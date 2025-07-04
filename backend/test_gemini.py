import google.generativeai as genai

# Paste your actual Gemini API key here
genai.configure(api_key="AIzaSyDss8aDYo4O9MxJQF2UYSIPaIl3ZRQdIL8")

try:
    models = genai.list_models()
    print("✅ Available models:")
    for m in models:
        print("-", m.name)
except Exception as e:
    print("❌ Error:", e)
