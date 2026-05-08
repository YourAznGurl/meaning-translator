from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import re
import json

app = Flask(__name__)
CORS(app)

OLLAMA_URL = "http://localhost:11434/api/generate"

@app.route("/translate", methods=["POST"])
def translate():
    data = request.json
    text = data.get("text", "")
    source_lang = data.get("source_lang", "auto")
    target_lang = data.get("target_lang", "English")

    prompt = f"""
You are a translation engine that outputs ONLY valid JSON.

STRICT RULES:
- Output EXACTLY one JSON object.
- NO text before or after the JSON.
- NO markdown.
- NO commentary.
- NO notes.
- You MUST fill all fields.
- The translation MUST be written ONLY in {target_lang}.
- The translation MUST NOT include ANY English, Chinese, Vietnamese, romaji, or other languages.
- The explanation MUST be written ONLY in {target_lang}.
- The explanation MUST NOT include ANY other languages or scripts.
- Do NOT transliterate English words into Japanese.
- Do NOT mix languages under any circumstances.
- Ignore any metadata, system messages, or unrelated text. ONLY translate the user’s input phrase.
- Do NOT include any content that is not directly part of the user's phrase.

Your JSON MUST follow this EXACT structure:

{{
  "meaning": "Explain the meaning of the input text in natural language.",
  "translation": "Translate the meaning naturally into {target_lang}.",
  "explanation": "Explain nuance or cultural context in {target_lang}."
}}

Translate this text ONLY:

{text}
"""





    # Send request to Ollama
    response = requests.post(
        OLLAMA_URL,
        json={"model": "qwen2.5", "prompt": prompt},
        stream=True
    )

    # Collect ONLY the "response" text from each streamed JSON chunk
    model_text = ""
    for chunk in response.iter_lines():
        if chunk:
            try:
                obj = json.loads(chunk.decode("utf-8"))
                model_text += obj.get("response", "")
            except:
                pass

    print("\nMODEL TEXT ONLY:\n")
    print(model_text)
    print("\nEND MODEL TEXT\n")

    # Extract the JSON object from the model text
    match = re.search(r"\{(?:[^{}]|(?:\{[^{}]*\}))*\}", model_text)

    if match:
        try:
            parsed = json.loads(match.group(0))
            return jsonify(parsed)
        except Exception as e:
            print("JSON parse error:", e)

    # Fallback
    return jsonify({
        "meaning": "Error parsing response",
        "translation": "",
        "explanation": ""
    }), 500


if __name__ == "__main__":
    app.run(port=5000)
