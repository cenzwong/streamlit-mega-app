import requests

# 
def ai21_rewrite(text, intent, key):

    url = "https://api.ai21.com/studio/v1/paraphrase"

    payload = {
        "style": f"{intent}",
        "text": f"{text}"
        }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": f"Bearer {key}"
    }

    response = requests.post(url, json=payload, headers=headers)
    response_json = response.json()
    response_json_suggestions = response_json.get("suggestions")
    

    return [t["text"] for t in response_json_suggestions]

def ai21_prompt(model, text, key):

    url = f"https://api.ai21.com/studio/v1/{model}/complete"

    payload = {
        "numResults": 1,
        "maxTokens": 16,
        "minTokens": 0,
        "temperature": 0.7,
        "topP": 1,
        "topKReturn": 0,
        "frequencyPenalty": {
            "scale": 1,
            "applyToWhitespaces": True,
            "applyToPunctuations": True,
            "applyToNumbers": True,
            "applyToStopwords": True,
            "applyToEmojis": True
        },
        "presencePenalty": {
            "scale": 0,
            "applyToWhitespaces": True,
            "applyToPunctuations": True,
            "applyToNumbers": True,
            "applyToStopwords": True,
            "applyToEmojis": True
        },
        "countPenalty": {
            "scale": 0,
            "applyToWhitespaces": True,
            "applyToPunctuations": True,
            "applyToNumbers": True,
            "applyToStopwords": True,
            "applyToEmojis": True
        },
        "prompt": f"{text}"
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": f"Bearer {key}"
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.json()["completions"][0]["data"]["text"]