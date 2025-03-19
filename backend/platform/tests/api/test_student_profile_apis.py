import pytest
from fastapi.testclient import TestClient
from ai_platform.apis.application import get_app

app = get_app()
client = TestClient(app)

def test_create_student_profile(client, db, student_auth_headers):
    payload = {
        "first_name": "John",
        "middle_name": "A",
        "last_name": "Doe",
        "email_id": "john.doe@iitm.ac.in"
    }
    response = client.post("/student-profile", json=payload, headers=student_auth_headers)
    assert response.status_code == 201
    assert response.json()["email_id"] == payload["email_id"]

def test_get_student_profile(client, student_auth_headers):
    response = client.get("/profile", headers=student_auth_headers)
    assert response.status_code == 200
    assert "first_name" in response.json()