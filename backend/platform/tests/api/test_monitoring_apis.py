import pytest
from fastapi.testclient import TestClient
from ai_platform.apis.application import get_app 

app = get_app()
client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"response": "ok"}