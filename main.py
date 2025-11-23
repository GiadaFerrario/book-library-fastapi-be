from fastapi import FastAPI

from database.database import engine, Base
from routers import books

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Book Library REST API")

app.include_router(books.router, prefix="/books", tags=["Books"])