from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

API_URL = "https://router.huggingface.co/hf-inference/models/distilbert/distilbert-base-uncased-finetuned-sst-2-english"


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

    if not text.strip():
        return {
            "error": "Input text cannot be empty"
        }

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
    flags = set()
    matched_words = set()

    lower_text = text.lower()

    lower_text = lower_text.replace("dont", "don't")

    weights = {
    "clickbait language": 8,
    "fear-based language": 12,
    "conspiracy phrasing": 15,
    "urgency manipulation": 10
    }

    patterns = {

        "clickbait language": [
            "breaking",
            "shocking",
            "unbelievable",
            "must watch",
            "you won't believe",
            "gone wrong",
            "viral",
            "exposed",
            "revealed",
            "jaw dropping",
            "insane",
            "this changes everything",
            "what happens next",
            "watch till the end",
            "mind blowing"
        ],

        "fear-based language": [
            "danger",
            "collapse",
            "crisis",
            "threat",
            "destroyed",
            "disaster",
            "catastrophe",
            "panic",
            "chaos",
            "deadly",
            "risk",
            "emergency",
            "terrifying",
            "warning",
            "unsafe"
        ],

        "conspiracy phrasing": [
            "hidden truth",
            "secret agenda",
            "wake up",
            "mainstream media",
            "they don't want you to know",
            "cover up",
            "deep state",
            "brainwashing",
            "propaganda",
            "media lies",
            "controlled narrative",
            "suppressed",
            "manipulated",
            "inside job",
            "government is hiding"
        ],

        "urgency manipulation": [
            "act now",
            "urgent",
            "before it's deleted",
            "share this immediately",
            "too late",
            "limited time",
            "don't ignore",
            "last chance",
            "right now",
            "immediately",
            "hurry",
            "time is running out",
            "fast",
            "spread this",
            "important"
        ]
    }

    for category, words in patterns.items():

        for word in words:

            if word in lower_text:

                if word not in matched_words:

                    score += weights[category]

                    matched_words.add(word)

                flags.add(category)

    letters = [c for c in text if c.isalpha()]

    uppercase_ratio = (
        sum(1 for c in letters if c.isupper())
        / max(len(letters), 1)
    )

    if uppercase_ratio > 0.5:

        score += 20
        flags.add("excessive capitalization")

    if sentiment["label"] == "NEGATIVE":

        score += int(sentiment["score"] * 40)

        flags.add("high emotional intensity")

    if score > 100:
        score = 100

    if score >= 70:
        severity = "HIGH"

    elif score >= 40:
        severity = "MEDIUM"
    else:
        severity = "LOW"

    return {

        "input_text": text,

        "sentiment": {
            "label": sentiment["label"],
            "score": round(sentiment["score"], 3)
        },

        "manipulation_score": score,
        "severity": severity,

        "flags": sorted(list(set(flags)))
    }


@app.get("/debug")
def debug():

    return {
        "token_exists": os.getenv("HF_TOKEN") is not None,
        "token_preview": str(os.getenv("HF_TOKEN"))[:10]
    }