import pytest
from fastapi.testclient import TestClient
from ai_platform.apis.application import get_app  

app = get_app()

client = TestClient(app)

def test_create_knowledge_base():
    response = client.post(
        "/create_knowledgebase",
        data={"vector_index": "test_index", "content": "Sample knowledge base content"}
    )
    assert response.status_code == 200
    assert response.json()["status"] is True

def test_read_agents():
    response = client.get("/agents/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_agent():
    agent_data = {"name": "Test Agent", "description": "Test Description"}
    response = client.post("/agents/", json=agent_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Test Agent"

def test_update_agent():
    agent_data = {"name": "Updated Agent", "description": "Updated Description"}
    response = client.put("/agents/1", json=agent_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Agent"

def test_delete_agent():
    response = client.delete("/agents/1")
    assert response.status_code == 200

def test_host_agent():
    request_data = {"message": "Hello", "history": [], "metadata": {"course_id": "1"}}
    response = client.post("/host_agent", json=request_data)
    assert response.status_code == 200

def test_openai_streaming():
    response = client.post("/openai_streaming")
    assert response.status_code == 200