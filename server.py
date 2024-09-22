""" Server """
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """ render index page """
    return render_template('index.html')

@app.route('/emotion_detector')
def emotion_detector_page():
    """ render emotion detector information """
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)

    dominant_emotion = result['emotions']['dominant_emotion']
    sadness = result['emotions']['sadness']
    joy = result['emotions']['joy']
    anger = result['emotions']['anger']
    disgust = result['emotions']['disgust']
    fear = result['emotions']['fear']
    message = 'For the given statement, the system response is \'anger\': {0}, \'disgust\': {1}, \'fear\': {2}, \'joy\': {3} and \'sadness\': {4}. The dominant emotion is {5}'.format(anger, disgust, fear, joy, sadness, dominant_emotion)
    if dominant_emotion == 'none':
        message = 'Invalid text! Please try again!.'

    return({'message': message}, result['code'])  # LF (\n)
    # End-of-file (EOF)