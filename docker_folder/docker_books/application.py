# Функціонал:
# 1. Отримання всіх книг
# ○  шлях – books
# ○  метод – GET

# 2.  Отримання даних за ID книги
# ○  шлях – books/{book_id}
# ○  метод – GET

# 3.  Додавання нової книги
# ○  шлях – books
# ○  метод – POST

# 4.  Видалення книги за ID
# ○  шлях – books/{book_id}
# ○  метод – DELETE

import fastapi
import json
import pydantic
from typing import List

class Book(pydantic.BaseModel):
    id: str
    title: str
    author: str
    year: int
    pages: int

app = fastapi.FastAPI()

@app.get("/books")
def get_all_books() -> List[Book]:
    with open("books.json", "r") as file:
        books = json.load(file)
        return books
