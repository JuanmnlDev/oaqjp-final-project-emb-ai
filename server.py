from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """ render index page """
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector_page():
    """ render emotionDetector page """
    text_to_analyze = request.args.get('textToAnalyze')
    emotions = emotion_detector(text_to_analyze)
    text = "For the given statement, the system response is '%d': 0.006274985, 'disgust': 0.0025598293, 'fear': 0.009251528, 'joy': 0.9680386 and 'sadness': 0.049744144. The dominant emotion is joy"
    print(text, (emotions['emotion']['dominant_emotion']))