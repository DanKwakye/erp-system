from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CustomerCreate(BaseModel):
    business_name: str
    customer_type: Optional[str] = None
    contact_person: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[str] = None
    is_active: bool = True

class CustomerUpdate(BaseModel):
    business_name: Optional[str] = None
    customer_type: Optional[str] = None
    contact_person: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[str] = None
    is_active: Optional[str] = None

class CustomerRead(BaseModel):
    customer_id: int
    business_name: str
    customer_type: Optional[str]
    contact_person: Optional[str]
    phone: Optional[str]
    location: Optional[str]
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime]


    class Config:
        from_attributes = True