from EmotionDetection import emotion_detector

def test_emotion():
    statements = [
        'I am glad this happened', 
        'I am really mad about this',
        'I feel disgusted just hearing about this', 
        'I am so sad about this', 
        'I am really afraid that this will happen'
    ]
    results = []
    for text_to_analyse in statements:
        result = emotion_detector(text_to_analyse)['dominant_emotion']
        results.append(result)

    return results