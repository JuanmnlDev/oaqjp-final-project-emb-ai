""" Module providing a function to detect emotions """
import requests

def emotion_detector(text_to_analyze):
    """ Function printing the text analized with emotions fron external API """
    # use the NLP Watson Library
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'  # URL of the sentiment analysis service
    myobj = { "raw_document": { "text": text_to_analyze } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    analized_text = response.text  # Return the response text from the API
    return analized_text  # Return the sentiment analysis result