import requests

def emotion_detector(text_to_analyse):
    """
    Ejecuta la detección de emociones utilizando IBM Watson Emotion Analysis API.
    Args:
        text_to_analyse (str): Texto de entrada para el análisis de emociones.
    Returns:
        dict: Diccionario con las emociones detectadas y sus respectivos puntajes.
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    payload = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        emotions = response.json()
        return emotions

    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")
        return None

# Ejemplo de uso
if __name__ == "__main__":
    sample_text = "Estoy muy emocionado por los avances en inteligencia artificial."
    detected_emotions = emotion_detector(sample_text)
    print("Emociones detectadas:", detected_emotions)
