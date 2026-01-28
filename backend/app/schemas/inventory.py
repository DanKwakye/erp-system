from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from decimal import Decimal

class InventoryMovementCreate(BaseModel):
    product_id: int
    movement_type: str
    quatity: Decimal
    reference_id: Optional[int] = None
    movement_date: datetime
    recorded_by: Optional[int] = None

class InventoryMovementUpdate(BaseModel):
    product_id: Optional[int] = None
    movement_type: Optional[str] = None
    quantity: Optional[Decimal] = None
    reference_id: Optional[int] = None
    movement_date: Optional[datetime] = None
    recorded_by: Optional[int] = None

class InventoryMovementRead(BaseModel):
    movement_id: int
    product_id: int
    movement_type: str
    quantity: Decimal
    reference_id: Optional[int]
    movement_date: datetime
    recorded_by: Optional[int]
    created_at: datetime


    class Config:
        from_attributes = True