"""Items API endpoints."""
from typing import List
from fastapi import APIRouter, HTTPException, status
from app.schemas.item import ItemCreate, ItemResponse

router = APIRouter(prefix="/api/items", tags=["Items"])

# In-memory storage for demo purposes
items_db: List[dict] = []
next_id = 1


@router.get("", response_model=List[ItemResponse])
async def get_items() -> List[ItemResponse]:
    """
    Get all items.
    
    Returns:
        List of all items
    """
    return items_db


@router.get("/{item_id}", response_model=ItemResponse)
async def get_item(item_id: int) -> ItemResponse:
    """
    Get a specific item by ID.
    
    Args:
        item_id: The ID of the item to retrieve
        
    Returns:
        The requested item
        
    Raises:
        HTTPException: If item not found
    """
    for item in items_db:
        if item["id"] == item_id:
            return item
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Item with id {item_id} not found"
    )


@router.post("", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemCreate) -> ItemResponse:
    """
    Create a new item.
    
    Args:
        item: Item data to create
        
    Returns:
        The created item with assigned ID
    """
    global next_id
    new_item = {
        "id": next_id,
        **item.model_dump()
    }
    items_db.append(new_item)
    next_id += 1
    return new_item
