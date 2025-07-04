from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# Replace this with your actual Gemini API key
genai.configure(api_key="AIzaSyDss8aDYo4O9MxJQF2UYSIPaIl3ZRQdIL8")  # 👈 your key here

model = genai.GenerativeModel("models/gemini-1.5-flash")




@app.route('/explain', methods=['POST'])
def explain():
    try:
        data = request.get_json()
        code = data.get("code", "")
        if not code:
            return jsonify({"error": "No code provided"}), 400

        prompt = f"Explain what this Python code does in simple terms:\n\n{code}"
        response = model.generate_content(prompt)
        explanation = response.text.strip()
        return jsonify({"explanation": explanation})

    except Exception as e:
        print(f"🔥 Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
