import uuid
from fastapi.testclient import TestClient
from ai_platform.apis.application import get_app  

app = get_app()

test_client = TestClient(app)

def test_create_conversation():
    response = test_client.post("/", json={"user_id": 1, "title": "New Conversation"})
    assert response.status_code == 200
    assert isinstance(response.json(), str)  # UUID as string

def test_get_conversation():
    conversation_id = uuid.uuid4()
    response = test_client.get(f"/{conversation_id}")
    assert response.status_code in [200, 404]

def test_get_user_conversation():
    user_id = 1
    response = test_client.get(f"/user/{user_id}")
    assert response.status_code in [200, 404]

def test_update_conversation():
    conversation_id = uuid.uuid4()
    response = test_client.put(f"/{conversation_id}", json={"title": "Updated Title"})
    assert response.status_code in [200, 404]

def test_delete_conversation():
    conversation_id = uuid.uuid4()
    response = test_client.delete(f"/{conversation_id}")
    assert response.status_code in [200, 404]