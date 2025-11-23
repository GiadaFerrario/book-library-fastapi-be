from fastapi import FastAPI

from routers import books

app = FastAPI(title="Book Library REST API")

app.include_router(books.router, prefix="/books", tags=["Books"])