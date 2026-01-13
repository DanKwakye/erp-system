from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Numeric
from sqlalchemy.sql import func
from app.core.database import Base

class OrderStatus(Base):
    __tablename__ = "order_statuses"

    status_id = Column(Integer, primary_key=True, index=True)
    status_name = Column(String(50), nullable=False, unique=True)

class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"), nullable=False)
    order_date = Column(DateTime(timezone=True), nullable=False)
    order_status = Column(String(50), default="pending")  # pending, delivered, cancelled
    total_amount = Column(Numeric(10, 2))
    created_by = Column(Integer, ForeignKey("staff.staff_id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class OrderItem(Base):
    __tablename__ = "order_items"
    order_item_id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.product_id"), nullable=False)
    quantity = Column(Numeric(10, 2), nullable=False)
    unit_price = Column(Numeric(10, 2), nullable=False)