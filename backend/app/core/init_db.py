from app.core.database import engine, Base

# Import all models so they're registered with Base
from app.models.product import Product, ProductCategory
from app.models.supplier import Supplier
from app.models.customer import Customer
from app.models.staff import Staff
from app.models.procurement import Procurement, ProcurementItem
from app.models.order import Order, OrderItem, OrderStatus
from app.models.inventory import InventoryMovement
from app.models.delivery import Delivery
from app.models.payment import Payment

def init_db():
    """Create all tables in the database"""
    Base.metadata.create_all(bind=engine)
    print("✅ All tables created successfully!")

if __name__ == "__main__":
    init_db()