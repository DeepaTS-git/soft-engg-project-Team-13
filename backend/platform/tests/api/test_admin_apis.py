import pytest
from fastapi.testclient import TestClient
from ai_platform.apis.application import get_app  

app = get_app()

client = TestClient(app)

def test_assign_course():
    response = client.post(
        "/ta/assign-course",
        json={"student_id": 1, "course_id": 1},
        headers={"Authorization": "Bearer testtoken"}
    )
    assert response.status_code in [200, 403, 404, 400]

def test_get_ungraded_assignments():
    response = client.get("/grade/assignment", headers={"Authorization": "Bearer testtoken"})
    assert response.status_code in [200, 404]

def test_grade_assignment():
    response = client.post(
        "/grade/assignment",
        json={"submission_id": 1, "score": 90},
        headers={"Authorization": "Bearer testtoken"}
    )
    assert response.status_code in [200, 404, 400]

def test_create_course():
    response = client.post(
        "/course/create",
        json={"name": "New Course", "description": "Course Description"},
        headers={"Authorization": "Bearer testtoken"}
    )
    assert response.status_code == 201

def test_get_course():
    response = client.get("/course/1", headers={"Authorization": "Bearer testtoken"})
    assert response.status_code in [200, 404]

def test_get_courses():
    response = client.get("/courses?skip=0&limit=10", headers={"Authorization": "Bearer testtoken"})
    assert response.status_code == 200

def test_update_course():
    response = client.put(
        "/course/1",
        json={"name": "Updated Course", "description": "Updated Description"},
        headers={"Authorization": "Bearer testtoken"}
    )
    assert response.status_code in [200, 404]

def test_delete_course():
    response = client.delete("/course/1", headers={"Authorization": "Bearer testtoken"})
    assert response.status_code in [200, 404]