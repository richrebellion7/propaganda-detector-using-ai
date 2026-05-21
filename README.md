# 📰 AI Propaganda Detector

A full-stack AI-powered web application that analyzes text for propaganda patterns, emotional manipulation, clickbait phrasing, conspiracy language, and urgency tactics.

## 🚀 Live Demo

Frontend:
https://propaganda-detector-using-ai-tazeem.streamlit.app/

Backend API:
https://propaganda-detector-using-ai-1.onrender.com/

---

## ✨ Features

- Propaganda pattern detection
- Clickbait analysis
- Fear-based language detection
- Conspiracy phrasing detection
- Urgency manipulation detection
- Emotional intensity scoring
- Severity classification (LOW / MEDIUM / HIGH)
- Duplicate phrase suppression
- Real-time AI sentiment analysis
- Cloud deployment with Streamlit + Render

---

## 🧠 Tech Stack

### Frontend
- Streamlit

### Backend
- FastAPI
- Python

### AI / NLP
- HuggingFace Inference API
- DistilBERT Sentiment Model

### Deployment
- Streamlit Cloud
- Render

---

## ⚙️ Architecture

User Input
↓
Streamlit Frontend
↓
FastAPI Backend
↓
HuggingFace Inference API
↓
Custom Heuristic Scoring Engine
↓
Severity Classification
↓
Frontend Visualization

---

## 📊 Example Detection

### Input
BREAKING! The mainstream media is hiding the hidden truth. Act now before this gets deleted!

### Output
- Severity: HIGH
- Manipulation Score: 92%
- Flags:
  - clickbait language
  - conspiracy phrasing
  - urgency manipulation
  - high emotional intensity

---

## 🛠️ Local Setup

### Clone repository

```bash
git clone https://github.com/richrebellion7/propaganda-detector-using-ai.git