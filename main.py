from fastapi import FastAPI
from models import TextInput
import hashlib

app = FastAPI(title="Token Generator API", description="API to generate pseudorandom tokens from text", version="1.0")

@app.get("/")
async def welcome():
    return {"message": "Welcome to the Token Generator API! Participant: Mark"}

def generate(text: str) -> str:
    checksum = hashlib.sha256(text.encode()).hexdigest()
    return checksum

@app.post("/generate-token/")
async def generate_token(input_data: TextInput):
    text = input_data.text
    token = generate(text)
    return {"text": text, "token": token}
