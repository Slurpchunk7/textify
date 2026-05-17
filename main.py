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

import random

words = [
    "lorem", "ipsum", "dolor", "sit", "amet",
    "consectetur", "adipiscing", "elit", "sed",
    "do", "eiusmod", "tempor", "incididunt",
    "ut", "labore", "et", "dolore", "magna", "aliqua",

    "enim", "ad", "minim", "veniam", "quis",
    "nostrud", "exercitation", "ullamco", "laboris",
    "nisi", "aliquip", "ex", "ea", "commodo",
    "consequat", "duis", "aute", "irure", "in",
    "reprehenderit", "voluptate", "velit", "esse",
    "cillum", "eu", "fugiat", "nulla", "pariatur",

    "excepteur", "sint", "occaecat", "cupidatat",
    "non", "proident", "sunt", "culpa", "qui",
    "officia", "deserunt", "mollit", "anim", "id",
    "est", "laborum", "praesent", "sapien", "massa",
    "convallis", "pellentesque", "habitant", "morbi",
    "tristique", "senectus", "netus", "malesuada",

    "fames", "ac", "turpis", "egestas", "integer",
    "eget", "aliquet", "nibh", "praesent", "tristique",
    "urna", "porttitor", "rhoncus", "dolor", "purus",
    "facilisis", "leo", "vel", "fringilla", "est",
    "ullamcorper", "eget", "nullam", "vehicula",
    "ipsum", "a", "arcu", "cursus", "vitae",

    "congue", "mauris", "rhoncus", "aenean",
    "pharetra", "magna", "vestibulum", "lectus",
    "mauris", "ultrices", "eros", "dictum",
    "fusce", "placerat", "orci", "nulla",
    "pellentesque", "dignissim", "enim", "sit",
    "amet", "venenatis", "urna", "cursus", "eget",

    "nunc", "scelerisque", "viverra", "mauris",
    "vitae", "ultricies", "leo", "integer",
    "malesuada", "nunc", "vel", "risus",
    "commodo", "viverra", "maecenas", "accumsan",
    "lacus", "vel", "facilisis", "volutpat",
    "est", "velit", "egestas", "dui"
]

@app.get("/lorem")
def generate_lorem(length: int = 50):
    text = []

    for _ in range(length ):
        text.append(random.choice(words))

    sentence = " ".join(text)
    sentence = sentence.capitalize() + "."

    return sentence

import hashlib

@app.get("/uuid5")
def uuid5(name: str, namespace: str = "12345678-1234-5678-1234-567812345678") -> str:
    ns = namespace.replace("-", "")
    ns_bytes = bytes.fromhex(ns)

    name_bytes = name.encode("utf-8")

    sha1 = hashlib.sha1(ns_bytes + name_bytes).digest()

    b = bytearray(sha1[:16])

    b[6] = (b[6] & 0x0F) | 0x50

    b[8] = (b[8] & 0x3F) | 0x80

    return (
        f"{b[0:4].hex()}-"
        f"{b[4:6].hex()}-"
        f"{b[6:8].hex()}-"
        f"{b[8:10].hex()}-"
        f"{b[10:16].hex()}"
    )

@app.get("/")
def home():
    return {"status": "online"}
