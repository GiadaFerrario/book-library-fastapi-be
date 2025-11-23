# Book Library REST API

A simple **Book Library backend** implemented with **FastAPI** for portfolio purposes.  
Provides basic CRUD operations for managing books.

---

## 🚀 Features

- List all books
- Get a single book by ID
- Add a new book
- Update an existing book
- Delete a book

All data is stored **in-memory** (no database).

---

## 📁 Project Structure

main.py # FastAPI app entrypoint
data/
  └─ in_memory_books.py # In memory db books
models/
  └─ book.py # Book data model
routers/
  └─ books.py # Books CRUD routes
requirements.txt # Python dependencies
