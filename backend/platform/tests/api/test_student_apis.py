import pytest
from fastapi.testclient import TestClient
from ai_platform.apis.application import get_app 

app = get_app()
client = TestClient(app)


def test_get_student_courses():
    response = client.get("/api/course/current", headers={"Authorization": "Bearer testtoken"})
    assert response.status_code in [200, 403, 404]
    if response.status_code == 200:
        assert isinstance(response.json(), list)

def test_get_course_content():
    course_id = 1  
    response = client.get(f"/api/course/{course_id}/weeks")
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        assert "course_id" in response.json()

def test_submit_assignment():
    submission_data = {
        "assignment_id": 1,
        "course_id": 1,
        "week_id": 1,
        "student_id": 1,
        "assignment_type": "graded",
        "submission_content": "Test submission content"
    }
    response = client.post("/api/assignment/submit", json=submission_data)
    assert response.status_code in [201, 404]
    if response.status_code == 201:
        assert "message" in response.json()
        assert "submission_id" in response.json()

def test_get_student_course_analytics():
    response = client.get("/api/analytics", headers={"Authorization": "Bearer testtoken"})
    assert response.status_code in [200, 403]
    if response.status_code == 200:
        assert isinstance(response.json(), list)
