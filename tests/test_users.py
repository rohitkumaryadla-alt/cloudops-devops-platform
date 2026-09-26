from fastapi.testclient import TestClient

from app.main import app

import uuid

client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_create_user():
    response = client.post(
        "/api/users",
        json={
            "name": "Test User",
            "email": "testuser@example.com"
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "Test User"
    assert data["email"] == "testuser@example.com"
    assert "id" in data

    user_id = data["id"]

    # Cleanup step
    delete_response = client.delete(f"/api/users/{user_id}")
    assert delete_response.status_code in (200, 204)


def test_get_users():
    response = client.get("/api/users")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_user_not_found():
    response = client.get("/api/users/999999")

    assert response.status_code == 404

def test_create_user_invalid_email():
    response = client.post(
        "/api/users",
        json={
            "name": "Invalid User",
            "email": "invalid-email"
        }
    )

    assert response.status_code == 422

def test_duplicate_email():
    
    email = f"duplicate_{uuid.uuid4().hex[:8]}@example.com"

    first_response = client.post(
        "/api/users",
        json={
            "name": "First User",
            "email": email
        }
    )
    assert first_response.status_code == 201

    second_response = client.post(
        "/api/users",
        json={
            "name": "Second User",
            "email": email
        }
    )
    assert second_response.status_code == 409