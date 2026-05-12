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

app = fastapi.FastAPI()


# ---------- МОДЕЛЬ ----------
class Film(pydantic.BaseModel):
    id: int
    title: str
    director: str
    year: int


# ---------- ОТРИМАТИ ВСІ ФІЛЬМИ ----------
@app.get("/films")
def get_films():

    with open("films.json", "r", encoding="utf-8") as file:
        films = json.load(file)

    return films


# ---------- ОТРИМАТИ ФІЛЬМ ПО ID ----------
@app.get("/films/{movie_id}")
def get_movie(movie_id: int):

    with open("films.json", "r", encoding="utf-8") as file:
        films = json.load(file)

    for film in films:
        if film["id"] == movie_id:
            return film

    return {"message": "Фільм не знайдено"}


# ---------- ДОДАТИ ФІЛЬМ ----------
@app.post("/films")
def add_movie(new_film: Film):

    with open("films.json", "r", encoding="utf-8") as file:
        films = json.load(file)

    films.append(new_film.dict())

    with open("films.json", "w", encoding="utf-8") as file:
        json.dump(films, file, ensure_ascii=False, indent=4)

    return {"message": "Фільм додано успішно"}


# ---------- ВИДАЛИТИ ФІЛЬМ ----------
@app.delete("/films/{movie_id}")
def delete_movie(movie_id: int):

    with open("films.json", "r", encoding="utf-8") as file:
        films = json.load(file)

    for film in films:
        if film["id"] == movie_id:
            films.remove(film)

            with open("films.json", "w", encoding="utf-8") as file:
                json.dump(films, file, ensure_ascii=False, indent=4)

            return {"message": "Фільм видалено"}

    return {"message": "Фільм не знайдено"}
