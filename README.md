# FastAPI Test Server

A production-ready FastAPI backend test server with industry standard folder structure and RESTful APIs.

## Features

- ✅ Industry-standard project structure
- ✅ FastAPI with automatic API documentation (Swagger UI & ReDoc)
- ✅ Three REST API endpoints (Health, Items, Users)
- ✅ Pydantic schemas for request/response validation
- ✅ CORS middleware configured
- ✅ Comprehensive test suite with pytest
- ✅ Type hints throughout

## Project Structure

```
fastapi_test_server/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application entry point
│   ├── api/                 # API route handlers
│   │   ├── __init__.py
│   │   ├── health.py        # Health check endpoint
│   │   ├── items.py         # Items CRUD endpoints
│   │   └── users.py         # Users CRUD endpoints
│   ├── core/                # Core functionality
│   │   ├── __init__.py
│   │   └── config.py        # Application settings
│   ├── models/              # Data models (for future database integration)
│   │   └── __init__.py
│   └── schemas/             # Pydantic schemas
│       ├── __init__.py
│       ├── item.py          # Item schemas
│       └── user.py          # User schemas
├── tests/                   # Test suite
│   ├── __init__.py
│   ├── test_main.py         # Tests for main app and health
│   ├── test_items.py        # Tests for items API
│   └── test_users.py        # Tests for users API
├── requirements.txt         # Python dependencies
├── pyproject.toml          # Project configuration
└── README.md               # This file
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/imramkrishna/fastapi_test_server.git
cd fastapi_test_server
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Server

Start the development server:

```bash
uvicorn app.main:app --reload
```

The server will start at `http://localhost:8000`

### Available Endpoints

- **Root**: `GET /` - Welcome message and API info
- **Health Check**: `GET /health` - Server health status
- **API Documentation**: 
  - Swagger UI: `http://localhost:8000/docs`
  - ReDoc: `http://localhost:8000/redoc`

## API Endpoints

### Items API

- `GET /api/items` - Get all items
- `GET /api/items/{item_id}` - Get a specific item
- `POST /api/items` - Create a new item

**Example Item:**
```json
{
  "name": "Laptop",
  "description": "High-performance laptop",
  "price": 999.99
}
```

### Users API

- `GET /api/users` - Get all users
- `GET /api/users/{user_id}` - Get a specific user
- `POST /api/users` - Create a new user

**Example User:**
```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "full_name": "John Doe"
}
```

## Testing

Run the test suite:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=app --cov-report=html
```

Run specific test file:

```bash
pytest tests/test_items.py
```

## Example Usage

### Using cURL

```bash
# Health check
curl http://localhost:8000/health

# Create an item
curl -X POST http://localhost:8000/api/items \
  -H "Content-Type: application/json" \
  -d '{"name":"Laptop","description":"High-performance laptop","price":999.99}'

# Get all items
curl http://localhost:8000/api/items

# Create a user
curl -X POST http://localhost:8000/api/users \
  -H "Content-Type: application/json" \
  -d '{"username":"john_doe","email":"john@example.com","full_name":"John Doe"}'

# Get all users
curl http://localhost:8000/api/users
```

### Using Python requests

```python
import requests

# Create an item
response = requests.post(
    "http://localhost:8000/api/items",
    json={
        "name": "Laptop",
        "description": "High-performance laptop",
        "price": 999.99
    }
)
print(response.json())

# Get all items
response = requests.get("http://localhost:8000/api/items")
print(response.json())
```

## Configuration

Settings can be configured via environment variables or a `.env` file:

```env
APP_NAME=FastAPI Test Server
APP_VERSION=1.0.0
DEBUG=true
```

## Development

### Code Style

The project follows PEP 8 style guidelines. All code includes type hints for better IDE support and maintainability.

### Adding New Endpoints

1. Create a new router in `app/api/`
2. Define Pydantic schemas in `app/schemas/`
3. Include the router in `app/main.py`
4. Add tests in `tests/`

## Technologies Used

- **FastAPI**: Modern, fast web framework for building APIs
- **Pydantic**: Data validation using Python type annotations
- **Uvicorn**: ASGI server for running FastAPI
- **pytest**: Testing framework
- **httpx**: HTTP client for testing

## License

MIT License

## Author

Ram Krishna
