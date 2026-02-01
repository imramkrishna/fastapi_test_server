"""Tests for items API endpoints."""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_items_db():
    """Reset the items database before each test."""
    from app.api import items
    items.items_db.clear()
    items.next_id = 1
    yield


def test_get_items_empty():
    """Test getting items when database is empty."""
    response = client.get("/api/items")
    assert response.status_code == 200
    assert response.json() == []


def test_create_item():
    """Test creating a new item."""
    item_data = {
        "name": "Test Item",
        "description": "A test item",
        "price": 10.99
    }
    response = client.post("/api/items", json=item_data)
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == item_data["name"]
    assert data["description"] == item_data["description"]
    assert data["price"] == item_data["price"]


def test_get_items_with_data():
    """Test getting items when database has data."""
    # Create an item first
    item_data = {
        "name": "Test Item",
        "description": "A test item",
        "price": 10.99
    }
    client.post("/api/items", json=item_data)
    
    # Get all items
    response = client.get("/api/items")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["name"] == item_data["name"]


def test_get_item_by_id():
    """Test getting a specific item by ID."""
    # Create an item first
    item_data = {
        "name": "Test Item",
        "description": "A test item",
        "price": 10.99
    }
    create_response = client.post("/api/items", json=item_data)
    item_id = create_response.json()["id"]
    
    # Get the item by ID
    response = client.get(f"/api/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == item_id
    assert data["name"] == item_data["name"]


def test_get_item_not_found():
    """Test getting a non-existent item."""
    response = client.get("/api/items/999")
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()


def test_create_item_invalid_price():
    """Test creating an item with invalid price."""
    item_data = {
        "name": "Test Item",
        "description": "A test item",
        "price": -10.99  # Invalid: negative price
    }
    response = client.post("/api/items", json=item_data)
    assert response.status_code == 422  # Validation error
