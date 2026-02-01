"""Users API endpoints."""
from typing import List
from fastapi import APIRouter, HTTPException, status
from app.schemas.user import UserCreate, UserResponse

router = APIRouter(prefix="/api/users", tags=["Users"])

# In-memory storage for demo purposes
users_db: List[dict] = []
next_id = 1


@router.get("", response_model=List[UserResponse])
async def get_users() -> List[UserResponse]:
    """
    Get all users.
    
    Returns:
        List of all users
    """
    return users_db


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int) -> UserResponse:
    """
    Get a specific user by ID.
    
    Args:
        user_id: The ID of the user to retrieve
        
    Returns:
        The requested user
        
    Raises:
        HTTPException: If user not found
    """
    for user in users_db:
        if user["id"] == user_id:
            return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with id {user_id} not found"
    )


@router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate) -> UserResponse:
    """
    Create a new user.
    
    Args:
        user: User data to create
        
    Returns:
        The created user with assigned ID
    """
    global next_id
    
    # Check if username or email already exists
    for existing_user in users_db:
        if existing_user["username"] == user.username:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already exists"
            )
        if existing_user["email"] == user.email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already exists"
            )
    
    new_user = {
        "id": next_id,
        **user.model_dump()
    }
    users_db.append(new_user)
    next_id += 1
    return new_user
