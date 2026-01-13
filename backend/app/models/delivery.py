from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base

class Delivery(Base):
    __tablename__ = "deliveries"
    
    delivery_id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"), nullable=False)
    delivery_date = Column(DateTime(timezone=True), nullable=False)
    delivery_status = Column(String(50), default="pending")
    delivered_by = Column(Integer, ForeignKey("staff.staff_id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())