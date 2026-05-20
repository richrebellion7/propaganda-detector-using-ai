from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI()


API_URL = "https://router.huggingface.co/hf-inference/models/distilbert/distilbert-base-uncased-finetuned-sst-2-english"

headers = {
    "Authorization": f"Bearer {os.getenv('HF_TOKEN')}"
}


class TextRequest(BaseModel):
    text: str


@app.get("/")
def home():
    return {
        "message": "AI Propaganda Detector API Running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/analyze")
def analyze(request: TextRequest):

    text = request.text

    payload = {
        "inputs": text
    }
    token = os.getenv("HF_TOKEN")

    headers = {
        "Authorization": f"Bearer {token}"
    }
    try:

        response = requests.post(
            API_URL,
            headers=headers,
            json=payload,
            timeout=60
        )

        print("STATUS CODE:", response.status_code)
        print("RAW RESPONSE:", response.text)

        result = response.json()

    except Exception as e:

        print("REQUEST ERROR:", e)

        return {
            "error": str(e)
        }

    if isinstance(result, dict) and "error" in result:

        return {
            "error": result["error"]
        }

    try:
        sentiment = result[0][0]

    except Exception as e:

        print("PARSING ERROR:", e)

        return {
            "error": "Failed to parse model response",
            "raw_response": result
        }


    score = 0
    flags = []

    lower_text = text.lower()

    clickbait_words = [
        "shocking",
        "breaking",
        "they don't want you to know",
        "must watch",
        "unbelievable",
        "secret truth",
        "wake up",
        "mainstream media"
    ]

    for word in clickbait_words:

        if word in lower_text:
            score += 20
            flags.append("clickbait language")

    if sentiment["label"] == "NEGATIVE":

        score += int(sentiment["score"] * 50)

        flags.append("high emotional intensity")

    if score > 100:
        score = 100

    return {

        "input_text": text,

        "sentiment": {
            "label": sentiment["label"],
            "score": round(sentiment["score"], 3)
        },

        "manipulation_score": score,

        "flags": list(set(flags))
    }

@app.get("/debug")
def debug():

    return {
        "token_exists": os.getenv("HF_TOKEN") is not None,
        "token_preview": str(os.getenv("HF_TOKEN"))[:10]
    }