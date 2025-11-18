from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/', methods=['GET'])
def home():
    # Render index.html from the templates folder
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET','POST'])
def emotion_detector_api():
    # Receive raw text from the request
    data = request.get_json()
    text = data.get('text', '')
    if not text:
        return jsonify({"error": "Missing text"}), 400

    result = emotion_detector(text)
    emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
    emotion_str = ', '.join(
        f"'{emo}': {result.get(emo)}" for emo in emotions[:-1]
    )
    emotion_str += f" and '{emotions[-1]}': {result.get(emotions[-1])}"
    formatted = (
        f"For the given statement, the system response is {emotion_str}. "
        f"The dominant emotion is {result.get('dominant_emotion')}."
    )

    return jsonify({"result": formatted})

# Flask automatically serves static files from /static and templates from /templates

if __name__ == '__main__':
    app.run(debug=True)
