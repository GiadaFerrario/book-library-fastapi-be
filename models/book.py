from typing import Optional
from pydantic import BaseModel

class Book(BaseModel):
    id: str
    title: str
    author: str
    year: int
    genre: str


class BookCreate(BaseModel):
    title: str
    author: str
    year: int
    genre: str


class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None
    genre: Optional[str] = None
