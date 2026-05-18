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
