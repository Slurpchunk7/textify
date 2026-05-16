from fastapi import FastAPI

app = FastAPI(title="Textify")

@app.get("/lowercase")
def to_lowercase(text: str): 
    return {"result": text.lower()}

@app.get("/uppercase")
def to_uppercase(text: str):
    return {"result": text.upper()}

@app.get("stats")
def stats(text: str):
    words = len(text.split())
    chars = len(text)

    return {
        "words": words,
        "characters": chars
    }

import base64

@app.get("/base64/encode")
def encode(text: str):
    return {
        "result": base64.b64encode(text.encode()).decode()
    }


@app.get("/base64/decode")
def decode(text: str):
    return {
        "result": base64.b64decode(text.encode()).decode()
    }

import re

@app.get("/slug")
def slug(text: str):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text.strip())
    return {"result": text}

@app.get("/")
def home():
    return {"status": "online"}