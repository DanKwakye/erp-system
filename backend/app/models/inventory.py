from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Numeric
from sqlalchemy.sql import func
from app.core.database import Base

class InventoryMovement(Base):
    __tablename__ = "inventory_movements"
    
    movement_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.product_id"), nullable=False)
    movement_type = Column(String(20), nullable=False)  # IN, OUT, SPOILAGE, ADJUSTMENT
    quantity = Column(Numeric(10, 2), nullable=False)
    reference_id = Column(Integer)  # order_id or procurement_id
    movement_date = Column(DateTime(timezone=True), nullable=False)
    recorded_by = Column(Integer, ForeignKey("staff.staff_id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())