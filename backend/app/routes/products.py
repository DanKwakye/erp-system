from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.models.product import Product, ProductCategory
from app.schemas.product import (
    ProductCreate, ProductRead, ProductUpdate,
    ProductCategoryCreate, ProductCategoryRead
)

router = APIRouter(prefix="/products", tags=["Products"])

#Product Category Endpoints

@router.post("/categories", response_model=ProductCategoryRead, status_code=201)
def create_category(category: ProductCategoryCreate, db: Session = Depends(get_db)):
    """Create a new product category"""
    db_category = ProductCategory(category_name=category.category_name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

@router.get("/categories", response_model=List[ProductCategoryRead])
def list_categories(db: Session = Depends(get_db)):
    """Get all product categories"""
    return db.query(ProductCategory).all()

# PRODUCT ENDPOINTS

@router.post("/", response_model=ProductRead, status_code=201)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    """Create a new product"""
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.get("/", response_model=List[ProductRead])
def list_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all products with pagination"""
    products = db.query(Product).offset(skip).limit(limit).all()
    return products

@router.get("/{product_id}", response_model=ProductRead)
def get_product(product_id: int, db: Session = Depends(get_db)):
    """Get a single product by ID"""
    product = db.query(Product).filter(Product.product_id ==product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/{product_id}", response_model=ProductRead)
def update_product(product_id: int, product_update: ProductUpdate = Body(...), db: Session = Depends(get_db)):
    """Update a product"""
    db_product = db.query(Product).filter(product_id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # Update only provided fields
    update_data = product_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_product, key, value)

    db.commit()
    db.refresh(db_product)
    return db_product

@router.delete("/{product_id}", status_code=204)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    """Delete a Product"""
    db_product = db.query(Product).filter(Product.product_id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, datail="Product not found")
    
    db.delete(db_product)
    db.commit()
    return None