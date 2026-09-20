from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
OLLAMA_API = "http://localhost:11434/api/generate"

def query_ollama(prompt, model="llama3"):
    response = requests.post(OLLAMA_API, json={
        "model": model,
        "prompt": prompt,
        "stream": False
    })
    return response.json().get("response", "No response")

@app.route("/analyze", methods=["POST"])
def analyze():
    user_text = request.json.get("text", "")
    emotion_prompt = f"Classify the emotion in this text: '{user_text}'. Respond with one word (happy, sad, stressed, angry)."
    emotion = query_ollama(emotion_prompt)

    resource_prompt = f"Suggest one coping strategy for someone who feels {emotion}."
    resource = query_ollama(resource_prompt)

    return jsonify({
        "emotion": emotion,
        "suggested_resource": resource
    })

if __name__ == "__main__":
    app.run(debug=True)
