from settings import settings

from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json


app = FastAPI()

# ---------- МОДЕЛЬ ----------
class Film(BaseModel):
    id: int
    title: str
    director: str
    year: int


# ---------- ОТРИМАТИ ВСІ ФІЛЬМИ ----------
@app.get("/films")
def get_films():

    with open(settings.data_file_path, "r", encoding="utf-8") as file:
        films = json.load(file)

    return films


# ---------- ОТРИМАТИ ФІЛЬМ ПО ID ----------
@app.get("/films/{movie_id}")
def get_movie(movie_id: int):

    with open(settings.data_file_path, "r", encoding="utf-8") as file:
        films = json.load(file)

    for film in films:
        if film["id"] == movie_id:
            return film

    return {"message": "Фільм не знайдено"}


# ---------- ДОДАТИ ФІЛЬМ ----------
@app.post("/films")
def add_movie(new_film: Film):

    with open(settings.data_file_path, "r", encoding="utf-8") as file:
        films = json.load(file)

    # ---------- MAX FILMS CHECK ----------
    if settings.max_films is not None:

        if len(films) >= settings.max_films:

            raise HTTPException(
                status_code=409,
                detail=f"Максимальна кількість фільмів: {settings.max_films}"
            )

    # ---------- ADD FILM ----------
    films.append(new_film.model_dump())

    with open(settings.data_file_path, "w", encoding="utf-8") as file:
        json.dump(films, file, ensure_ascii=False, indent=4)

    return {"message": "Фільм додано успішно"}

# ---------- ВИДАЛИТИ ФІЛЬМ ----------
@app.delete("/films/{movie_id}")
def delete_movie(movie_id: int):

    with open(settings.data_file_path, "r", encoding="utf-8") as file:
        films = json.load(file)

    for film in films:
        if film["id"] == movie_id:
            films.remove(film)

            with open(settings.data_file_path, "w", encoding="utf-8") as file:
                json.dump(films, file, ensure_ascii=False, indent=4)

            return {"message": "Фільм видалено"}

    return {"message": "Фільм не знайдено"}
