""" Module providing a function to detect emotions """
import requests
import json

def emotion_detector(text_to_analyze):
    """ Function printing the text analized with emotions fron external API """
    # use the NLP Watson Library
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the sentiment analysis service
    myobj = { "raw_document": { "text": text_to_analyze } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header, timeout = 300)  # Send a POST request to the API with the text and headers
    formatted_response = json.loads(response.text)  # convert response text into a dictionary
    
    emotions_predictions = formatted_response['emotionPredictions'][0]['emotion']

    emotions_array = [
        {'label': 'anger', 'value': emotions_predictions['anger']},
        {'label': 'disgust', 'value': emotions_predictions['disgust']},
        {'label': 'fear', 'value': emotions_predictions['fear']},
        {'label': 'joy', 'value': emotions_predictions['joy']},
        {'label': 'sadness', 'value': emotions_predictions['sadness']}
    ]

    dominant_emotion = {}

    for emotion in emotions_array:
        if dominant_emotion == {} or emotion['value'] > dominant_emotion['value']:
            dominant_emotion = emotion

    
    emotions = {
        'anger': emotions_predictions['anger'],
        'disgust': emotions_predictions['disgust'],
        'fear': emotions_predictions['fear'],
        'joy': emotions_predictions['joy'],
        'sadness': emotions_predictions['sadness'],
        'dominant_emotion': dominant_emotion['label']
    }

    return ({'emotions': emotions})