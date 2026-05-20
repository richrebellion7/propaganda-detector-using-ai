from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

app = FastAPI()
class TextRequest(BaseModel):
    text: str

classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

@app.get("/")
def home():
    return {"message": "Propaganda Detector API Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/analyze")
def analyze(request: TextRequest):
    text = request.text

    result = classifier(text)

    score = 0
    flags = []

    lower_text = text.lower()

    clickbait_words = [
        "shocking",
        "breaking",
        "they don't want you to know",
        "must watch",
        "unbelievable"
    ]

    for word in clickbait_words:
        if word in lower_text:
            score += 20
            flags.append("clickbait language")

    sentiment = result[0]

    if sentiment["label"] == "NEGATIVE":
        score += int(sentiment["score"] * 50)
        flags.append("high emotional intensity")

    if score > 100:
        score = 100

    return {
        "input_text": text,
        "sentiment": sentiment,
        "manipulation_score": score,
        "flags": list(set(flags))
    }