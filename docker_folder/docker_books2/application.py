from settings import settings

from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int
    pages: int


@app.get("/books/")
def all_books() -> List[Book]:

    with open(settings.data_file_path) as file:

        books = json.load(file)

    return books


@app.get("/books/{id}")
def get_book(id: int):

    with open(settings.data_file_path) as file:

        books = json.load(file)

    for book in books:

        if book["id"] == id:
            return book


@app.post("/books/")
def create_book(book: Book) -> dict[str, str]:

    with open(settings.data_file_path) as file:

        books = json.load(file)

    # --- ПЕРЕВІРКА КІЛЬКОСТІ КНИГ ---
    if settings.max_books is not None:

        if len[books] >= settings.max_books:
            raise HTTPException(
                status_code=409,
                detail=f"Maximum number of books is {settings.max_books}"
            )

    books.append(book.model_dump())

    with open(settings.data_file_path, "w") as file:

        json.dump(books, file, indent=4)

    return {"message": "Книга додана успішно"}

# ---- SELECT BY AUTHOR -----
@app.get("/select/author")
def get_books_by_author(author: str):

    with open(settings.data_file_path) as file:

        books = json.load(file)

    author_books = []

    for book in books:

        if book["author"].lower() == author.lower():

            author_books.append(book)

    return author_books
