import pytest
from fastapi.testclient import TestClient
from ai_platform.apis.application import get_app

app = get_app()

client = TestClient(app)


@pytest.fixture
def auth_headers():
    return {"Authorization": "Bearer test_token"}


def test_register_courses(auth_headers):
    payload = {"course_ids": [1, 2, 3]}
    response = client.post("/register-courses", json=payload, headers=auth_headers)
    assert response.status_code in [200, 201]
    assert isinstance(response.json(), list)
    

def test_get_course_content(auth_headers):
    course_id = 1
    response = client.get(f"/courses/{course_id}", headers=auth_headers)
    assert response.status_code == 200
    assert "weeks" in response.json()
    

def test_get_student_deadlines(auth_headers):
    response = client.get("/deadlines", headers=auth_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
