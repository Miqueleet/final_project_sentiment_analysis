import requests
import json

def emotion_detector(text_to_analyse):
         
    
    if text_to_analyse == "":


         dictio = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
         }

    else:  
        URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
        hdrs = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
        input = { "raw_document": { "text": text_to_analyse } }
        response = requests.post(URL, json = input, headers=hdrs)  
        formatted_response = json.loads(response.text)
    
    
        dictio = formatted_response['emotionPredictions'][0]['emotion']
        dictio['dominant_emotion'] = max(dictio, key=dictio.get)   


    return dictio
    