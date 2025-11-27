from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.config import get_db
from database.models import Product, InactiveProduct   # 👈 ADD THIS

router = APIRouter()

@router.get("/products")
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

@router.get("/inactive-products")
def get_inactive_products(db: Session = Depends(get_db)):
    return db.query(InactiveProduct).all()
