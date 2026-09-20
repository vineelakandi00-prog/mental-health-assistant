from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    user_text = data.get("text", "")

    # Simple emotion detection (placeholder logic)
    if "sad" in user_text.lower():
        emotion = "Sad"
        strategy = "Try deep breathing or listening to calming music."
    elif "happy" in user_text.lower():
        emotion = "Happy"
        strategy = "Keep a gratitude journal to capture this feeling."
    elif "angry" in user_text.lower():
        emotion = "Angry"
        strategy = "Take a few minutes to cool down and practice mindfulness."
    else:
        emotion = "Neutral"
        strategy = "Write down your thoughts to clear your mind."

    return jsonify({"emotion": emotion, "strategy": strategy})

if __name__ == "__main__":
    app.run(debug=True)
