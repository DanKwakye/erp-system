from pydantic import BaseModel
from datetime import datetime


class SupplierCreate(BaseModel):
    supplier_name: str
    supplier_type: str | None = None
    phone: str | None = None
    location: str | None = None
    is_active: bool = True


class SupplierUpdate(BaseModel):
    supplier_name: str | None = None
    supplier_type: str | None = None
    phone: str | None = None
    location: str | None = None
    is_active: bool | None = None


class SupplierRead(BaseModel):
    supplier_id: int
    supplier_name: str
    supplier_type: str | None = None
    phone: str | None = None
    location: str | None = None
    is_active: bool
    created_at: datetime
    updated_at: datetime | None = None
    
    class Config:
        from_attributes = True