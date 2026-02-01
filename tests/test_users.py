"""Tests for users API endpoints."""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_users_db():
    """Reset the users database before each test."""
    from app.api import users
    users.users_db.clear()
    users.next_id = 1
    yield


def test_get_users_empty():
    """Test getting users when database is empty."""
    response = client.get("/api/users")
    assert response.status_code == 200
    assert response.json() == []


def test_create_user():
    """Test creating a new user."""
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "full_name": "Test User"
    }
    response = client.post("/api/users", json=user_data)
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["username"] == user_data["username"]
    assert data["email"] == user_data["email"]
    assert data["full_name"] == user_data["full_name"]


def test_get_users_with_data():
    """Test getting users when database has data."""
    # Create a user first
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "full_name": "Test User"
    }
    client.post("/api/users", json=user_data)
    
    # Get all users
    response = client.get("/api/users")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["username"] == user_data["username"]


def test_get_user_by_id():
    """Test getting a specific user by ID."""
    # Create a user first
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "full_name": "Test User"
    }
    create_response = client.post("/api/users", json=user_data)
    user_id = create_response.json()["id"]
    
    # Get the user by ID
    response = client.get(f"/api/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id
    assert data["username"] == user_data["username"]


def test_get_user_not_found():
    """Test getting a non-existent user."""
    response = client.get("/api/users/999")
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()


def test_create_user_duplicate_username():
    """Test creating a user with duplicate username."""
    user_data = {
        "username": "testuser",
        "email": "test1@example.com",
        "full_name": "Test User 1"
    }
    client.post("/api/users", json=user_data)
    
    # Try to create another user with the same username
    duplicate_data = {
        "username": "testuser",
        "email": "test2@example.com",
        "full_name": "Test User 2"
    }
    response = client.post("/api/users", json=duplicate_data)
    assert response.status_code == 400
    assert "username" in response.json()["detail"].lower()


def test_create_user_duplicate_email():
    """Test creating a user with duplicate email."""
    user_data = {
        "username": "testuser1",
        "email": "test@example.com",
        "full_name": "Test User 1"
    }
    client.post("/api/users", json=user_data)
    
    # Try to create another user with the same email
    duplicate_data = {
        "username": "testuser2",
        "email": "test@example.com",
        "full_name": "Test User 2"
    }
    response = client.post("/api/users", json=duplicate_data)
    assert response.status_code == 400
    assert "email" in response.json()["detail"].lower()


def test_create_user_invalid_email():
    """Test creating a user with invalid email."""
    user_data = {
        "username": "testuser",
        "email": "invalid-email",
        "full_name": "Test User"
    }
    response = client.post("/api/users", json=user_data)
    assert response.status_code == 422  # Validation error
