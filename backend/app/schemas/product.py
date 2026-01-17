from pydantic import BaseModel
from typing import Optional
from datetime import datetime

#Schema for creating a product category
class ProductCategoryCreate(BaseModel):
    category_name:str

#Schema for reading a product category (with ID)
class ProductCategoryRead(BaseModel):
    category_id: int
    category_name: str
    created_at: datetime

    class Config:
        from_attributes = True #Allows conversion from SQLAlchemy model

# Schema for creating a product
class ProductCreate(BaseModel):
    product_name: str
    category_id: Optional[int] = None
    unit_of_measure: Optional[str] = None
    perishability_days: Optional[int] = None
    is_active: bool = True

# Schema for updating a product
class ProductUpdate(BaseModel):
    product_name: Optional[str] = None
    category_id: Optional[int] = None
    unit_of_measure: Optional[str] = None
    perishability_days: Optional[int] = None
    is_active: Optional[bool] = None

# Schema for reading a product (with ID and timestamps)
class ProductRead(BaseModel):
    product_id: int
    product_name: str
    category_id: Optional[int]
    unit_of_measure: Optional[str]
    perishability_days: Optional[int]
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime]


class Config:
    from_attributes = True