from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/', methods=['GET'])
def home():
    """
    Render the main index.html page.

    Returns:
        Rendered HTML template for the home page.
    """
    # Render index.html from the templates folder
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET','POST'])
def emotion_detector_api():
    """
    Handle emotion detection requests.

    - For GET requests, expects 'textToAnalyze' as a query parameter.
    - For POST requests, expects JSON body with a 'text' field.
    - Returns formatted emotion analysis or error message.

    Returns:
        str: Formatted string with emotion results or error HTML.
    """
    # Receive raw text from the request
    if request.method == 'GET':
        text = request.args.get('textToAnalyze', '')
    else:
        data = request.get_json()
        text = data.get('text', '') if data else ''

    result = emotion_detector(text)

    if result.get('dominant_emotion') == None:
        return '<b>Invalid text! Please try again!</b>'

    emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
    emotion_str = ', '.join(
        f"'{emo}': {result.get(emo)}" for emo in emotions[:-1]
    )
    emotion_str += f" and '{emotions[-1]}': {result.get(emotions[-1])}"
    formatted = (
    f"For the given statement, the system response is {emotion_str}. "
    f"The dominant emotion is <b>{result.get('dominant_emotion')}</b>."
)

    return formatted

# Flask automatically serves static files from /static and templates from /templates

if __name__ == '__main__':
    app.run(debug=True)
