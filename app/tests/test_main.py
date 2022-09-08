from fastapi.testclient import TestClient

from app import main

client = TestClient(app)


def get():
    response = client.get("/")
    assert response.status_code == 200
