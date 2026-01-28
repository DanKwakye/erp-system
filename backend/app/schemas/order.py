from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from decimal import Decimal

# Order Item Schemas
class OrderItemCreate(BaseModel):
    product_id: int
    quantity: Decimal
    unit_price: Decimal

class OrderItemRead(BaseModel):
    order_item_id: int
    order_id: int
    product_id: int
    quantity: Decimal
    unit_price: Decimal

    class Config:
        from_attribute = True

    
# Order Schemas
class OrderCreate(BaseModel):
    customer_id: int
    order_date: datetime
    order_status: str ="pending"
    total_amount: Decimal
    created_by: Optional[int] = None
    order_items: List[OrderItemCreate]

class OrderUpdate(BaseModel):
    customer_id: Optional[int] = None
    order_date: Optional[datetime] = None
    order_status: Optional[str] = None
    total_amount: Optional[Decimal] = None

class OrderRead(BaseModel):
    order_id: int
    customer_id: int
    order_date: datetime
    order_status: str
    total_amount: Decimal
    created_by: Optional[int]
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True