from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Numeric
from sqlalchemy.sql import func
from app.core.database import Base

class Procurement(Base):
    __tablename__ = "procurements"

    procurement_id = Column(Integer, primary_key=True, index=True)
    supplier_id = Column(Integer, ForeignKey("suppliers.supplier_id"), nullable=False)
    procurement_date = Column(DateTime(timezone=True), nullable=False)
    total_cost = Column(Numeric(10, 2))
    recorded_by = Column(Integer, ForeignKey("staff.staff_id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class ProcurementItem(Base):
    __tablename__ = "procurement_items"

    procurement_item_id = Column(Integer, primary_key=True, index=True)
    procurement_id = Column(Integer, ForeignKey("procurements.procurement_id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.product_id"), nullable=False)
    quantity = Column(Numeric(10, 2), nullable=False)
    unit_cost = Column(Numeric(10, 2), nullable=False)
