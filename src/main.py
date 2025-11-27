from fastapi import FastAPI
from routers import upload, products
from database.models import Base
from database.config import engine

app = FastAPI()

# create tables
Base.metadata.create_all(bind=engine)

app.include_router(upload.router)
app.include_router(products.router)
