import requests

def emotion_detector(text_to_analyse):
    """
    Sends text to an emotion detection API and returns predicted emotions.

    Parameters:
    text_to_analyse (str): The string of text to analyze for emotions.

    Returns:
    dict: A dictionary containing emotions scores and the dominant emotion.
          If the API response status is 400, all values are None.
    """

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    json_data = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    response = requests.post(url, headers=headers, json=json_data)

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    results = response.json()['emotionPredictions'][0]['emotion']
    results['dominant_emotion'] = max(results, key=results.get)


    return results
