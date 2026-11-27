from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["project"] == "CloudPilot"
    assert data["status"] == "running"
    assert data["message"] == "Welcome to CloudPilot Platform"
