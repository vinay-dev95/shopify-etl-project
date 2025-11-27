# database/models.py

# database/models.py

from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, DateTime, func
from database.config import Base
from datetime import datetime

class Product(Base):
    __tablename__ = "products"   # table name

    id = Column(Integer, primary_key=True, index=True)
    device_name = Column(String)
    variant_grams = Column(Float)
    vendor = Column(String)
    variant_sku = Column(String)
    variant_inventory_tracker = Column(String)
    status = Column(String)
    variant_type = Column(String)
    variant_price = Column(Float)
    created_at = Column(TIMESTAMP, server_default=func.now())


class InactiveProduct(Base):
    __tablename__ = "inactive_products"

    id = Column(Integer, primary_key=True, index=True)
    device_name = Column(String)
    variant_grams = Column(Float)
    vendor = Column(String)
    variant_sku = Column(String)
    variant_inventory_tracker = Column(String)
    status = Column(String)
    variant_type = Column(String)
    variant_price = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

