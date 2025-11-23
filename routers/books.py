from typing import List

from fastapi import APIRouter, HTTPException
from models.book import Book, BookCreate, BookUpdate

router = APIRouter()

@router.get("/", response_model=List[Book])
def get_books():
    return books


@router.get("/{book_id}", response_model=Book)
def get_book(book_id: str):
    book = next((b for b in books if b.id == book_id), None)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.post("/", response_model=Book)
def add_book(data: BookCreate):
    new_book = Book(
        id=str(len(books) + 1),
        title=data.title,
        author=data.author,
        year=data.year,
        genre=data.genre,
    )
    books.append(new_book)
    return new_book


@router.put("/{book_id}", response_model=Book)
def update_book(book_id: str, data: BookUpdate):
    book = next((b for b in books if b.id == book_id), None)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    if data.title is not None:
        book.title = data.title
    if data.author is not None:
        book.author = data.author
    if data.year is not None:
        book.year = data.year
    if data.genre is not None:
        book.genre = data.genre
    return book


@router.delete("/{book_id}", response_model=Book)
def delete_book(book_id: str):
    global books
    book = next((b for b in books if b.id == book_id), None)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    books = [b for b in books if b.id != book_id]
    return book