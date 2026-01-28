from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from sqlalchemy import func as sql_func
from typing import List

from app.core.database import get_db
from app.models.inventory import InventoryMovement
from app.schemas.inventory import InventoryMovementCreate, InventoryMovementRead, InventoryMovementUpdate

router = APIRouter(prefix="/inventory", tags=["Inventory"])

@router.post("/movements", response_model=InventoryMovementRead, status_code=201)
def create_movement(movement: InventoryMovementCreate, db: Session = Depends(get_db)):
    """Create a new inventory movement"""
    db_movement = InventoryMovement(**movement.dict())
    db.add(db_movement)
    db.commit()
    db.refresh(db_movement)
    return db_movement

@router.get("/movements", response_model=List[InventoryMovementRead])
def list_movements(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all inventory movements"""
    movements = db.query(InventoryMovement).offset(skip).limit(limit).all()
    return movements

@router.get("/movements?{movement_id}", response_model=InventoryMovementRead)
def get_movement(movement_id: int, db: Session = Depends(get_db)):
    """Get a single movement by ID"""
    movement = db.query(InventoryMovement).filter(InventoryMovement.movement_id == movement_id).first()
    if not movement:
        raise HTTPException(status_code=404, detail="Movement not found")
    return movement

@router.get("/stock{product_id}")
def get_current_stock(product_id: int, db: Session = Depends(get_db)):
    """Get current stock level for a product"""
    # Calculate stock: IN movements - OUT/SPOILAGE movements
    stock_in = db.query(func.sum(InventoryMovement.quantity)).filter(
        InventoryMovement.product_id == product_id,
        InventoryMovement.movement_type == 'IN'
    ).scalar() or 0

    stock_out = db.query(func.sum(InventoryMovement.quantity)).filter(
        InventoryMovement.product_id == product_id,
        InventoryMovement.movement_type.in_(['OUT', 'SPOILAGE'])
    ).scalar() or 0

    current_stock = stock_in - stock_out

    return {
        "product_id": product_id,
        "current_stock": float(current_stock),
        "stock_in": float(stock_in),
        "stock_out": float(stock_out)
    }

@router.delete("/movements/{movement_id}", status_code=204)
def delete_movement(movement_id: int, db: Session = Depends(get_db)):
    """Delete a movement"""
    db_movement = db.query(InventoryMovement).filter(InventoryMovement.movement_id == movement_id).first()
    if not db_movement:
        raise HTTPException(status_code=404, detail="Movement not found")
    
    db.delete(db_movement)
    db.commit()
    return None