# Курс: AI+Python
# Модуль 14. Мережеве програмування
# Тема: Мережеве програмування. Частина 2

#   Завдання 1
# Напишіть сервер для збереження даних про фільми.
# Дані знаходяться у файлі films.json
# Напишіть модель на pydentic з такими даними:
# ● id
# ● title
# ● director
# ● year

# Функціонал:
# 1. Отримання даних за ID фільму
# ○ шлях – movies/{movie_id}
# ○ метод – GET

# 2. Додавання нового фільму
# ○ шлях – movies
# ○ метод – POST

# 3. Видалення фільму за ID
# ○ шлях – movies/{movie_id}
# ○ метод – DELETE

# Запустіть сервер
# Напишіть клієнта з таким функціоналом для користувача:
# ● отримати дані про фільм
# ● додати новий фільм
# ● видалити фільм

import fastapi
import json
import pydantic
from typing import List

class Films(pydantic.BaseModel):
    id: str
    title: str
    director: str
    year: int

app = fastapi.FastAPI()

@app.get("/films")
def get_films() -> List[Films]:
    with open("films.json", 'r') as file:
        films = json.load(file)
        return films
