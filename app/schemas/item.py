"""Item schemas for request/response validation."""
from typing import Optional
from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    """Base item schema."""
    name: str = Field(..., min_length=1, max_length=100, description="Item name")
    description: Optional[str] = Field(None, max_length=500, description="Item description")
    price: float = Field(..., gt=0, description="Item price")


class ItemCreate(ItemBase):
    """Schema for creating an item."""
    pass


class ItemResponse(ItemBase):
    """Schema for item response."""
    id: int = Field(..., description="Item ID")
    
    class Config:
        """Pydantic configuration."""
        from_attributes = True
