from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_welcome():
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome" in response.json()["message"]

def test_generate_token():
    payload = {"text": "Hello World"}
    response = client.post("/generate-token/", json=payload)
    assert response.status_code == 200
    assert response.json()["text"] == "Hello World"
    assert len(response.json()["token"]) == 64
