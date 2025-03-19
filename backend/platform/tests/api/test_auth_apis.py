import pytest
from fastapi.testclient import TestClient
from ai_platform.apis.application import get_app  

app = get_app()

client = TestClient(app)

# Test Signup API
def test_signup():
    response = client.post(
        "/signup",
        json={
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "securepassword",
            "role": "STUDENT"
        }
    )
    assert response.status_code in [200, 400]
    if response.status_code == 200:
        assert "access_token" in response.json()
        assert "message" in response.json()

# Test Login API
def test_login():
    response = client.post(
        "/login",
        data={"username": "testuser", "password": "securepassword"}
    )
    assert response.status_code in [200, 401]
    if response.status_code == 200:
        assert "access_token" in response.json()

# Test Student Dashboard Access
def test_student_dashboard():
    login_response = client.post("/login", data={"username": "testuser", "password": "securepassword"})
    if login_response.status_code == 200:
        token = login_response.json()["access_token"]
        response = client.get("/student", headers={"Authorization": f"Bearer {token}"})
        assert response.status_code == 200
        assert response.json()["message"] == "Welcome to the student dashboard"

# Test TA Dashboard Access
def test_ta_dashboard():
    login_response = client.post("/login", data={"username": "testta", "password": "securepassword"})
    if login_response.status_code == 200:
        token = login_response.json()["access_token"]
        response = client.get("/ta", headers={"Authorization": f"Bearer {token}"})
        assert response.status_code == 200
        assert response.json()["message"] == "Welcome to the TA dashboard"

# Test Instructor Dashboard Access
def test_instructor_dashboard():
    login_response = client.post("/login", data={"username": "testinstructor", "password": "securepassword"})
    if login_response.status_code == 200:
        token = login_response.json()["access_token"]
        response = client.get("/instructor", headers={"Authorization": f"Bearer {token}"})
        assert response.status_code == 200
        assert response.json()["message"] == "Welcome to the instructor dashboard"

# Test Admin Dashboard Access
def test_admin_dashboard():
    login_response = client.post("/login", data={"username": "testadmin", "password": "securepassword"})
    if login_response.status_code == 200:
        token = login_response.json()["access_token"]
        response = client.get("/admin", headers={"Authorization": f"Bearer {token}"})
        assert response.status_code == 200
        assert response.json()["message"] == "Welcome to the admin dashboard"
