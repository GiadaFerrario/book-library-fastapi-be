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

main.py                     # FastAPI app entrypoint
pydantic_schemas/
  └─ book.py                # Pydantic schemas
database/
  ├─ database.py            # engine, SessionLocal, Base, get_db()
  └─ models/
       └─ book.py           # SQLAlchemy ORM model
routers/
  └─ books.py               # CRUD routes
requirements.txt

---

## 🛠️ Next Steps

- Add 'Genre' router endpoints and model