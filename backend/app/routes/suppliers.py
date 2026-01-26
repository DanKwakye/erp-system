from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.models.supplier import Supplier
from app.schemas.supplier import SupplierCreate, SupplierRead, SupplierUpdate

router = APIRouter(prefix="/suppliers", tags=["Suppliers"])

@router.post("/", response_model=SupplierRead, status_code=201)
def create_supplier(supplier: SupplierCreate, db: Session = Depends(get_db)):
    "Create a new Supplier"
    db_supplier = Supplier(**supplier.dict())
    db.add(db_supplier)
    db.commit()
    db.refresh(db_supplier)
    return db_supplier

@router.get("/", response_model=List[SupplierRead])
def list_suppliers(skip: int = 0, limit: int=100, db: Session = Depends(get_db)):
        """Get all suppliers with pagination"""
        suppliers = db.query(Supplier).offset(skip).limit(limit).all()
        return suppliers

@router.get("/{supplier_id}", response_model=SupplierRead)
def get_supplier(supplier_id: int, db: Session = Depends(get_db)):
      """Get a single supplier by ID"""
      supplier = db.query(Supplier).filter(Supplier.supplier_id == supplier_id).first()
      if not supplier:
            raise HTTPException(status_code=404, detail="Supplier not found")
      return supplier

@router.put("/{supplier_id}", response_model=SupplierRead)
def update_supplier(supplier_id: int, supplier_update: SupplierUpdate, db: Session = Depends(get_db)):
      "Update a supplier"
      db_supplier = db.query(Supplier).filter(Supplier.supplier_id == supplier_id).first()
      if not db_supplier:
            raise HTTPException(status_code=404, detail="Supplier not found")
      
      update_data = supplier_update.update.dict(exclude_unset=True)
      for key, value in update_data.items():
            setattr(db_supplier, key, value)

      db.commit()
      db.refresh(db_supplier)
      return db_supplier

@router.delete("/{supplier_id}", status_code=204)
def delete_supplier(supplier_id: int, db: Session = Depends(get_db)):
    "Delete a supplier"
    db_supplier = db.query(Supplier).filter(Supplier.supplier_id == supplier_id).first()
    if not db_supplier:
          raise HTTPException(status_code=404, detail="Supplier not found")
    
    db.delete(db_supplier)
    db.commit()
    return None