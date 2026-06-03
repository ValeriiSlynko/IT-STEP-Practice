# Курс: AI+Python
# Модуль 14. Серверне програмування
# Тема: Docker. Частина 1

#   ЗАВДАННЯ 1
# Напишіть код, який раз в 2 секунди виводить на екран:
# ● версію пайтона
# ● фразу “hello”
# ● версію бібліотеки pydantic
# ● час коли почала працювати програма
# див time.sleep() datetime.datetime.now()

# Створіть Dockerfile:
# ● python:3.11-slim
# ● робоча директорія – /app
# ● встановіть pydantic версії 2.6.4
# ● скопіюйте увесь код
# ● запустіть основний файл

# Створіть образ pydantic-loop
# docker build -t pydantic-loop .

# Cтворіть два контейнера test1 test2
# docker run -d –-name test1 pydantic-loop

# Подивіться на свої зображення:  docker images
# Подивіться на контейнери:  docker ps
# Подивіться логи обох контейнерів(має відрізнятись час):  docker logs -f test1
# Зупиніть контейнер test1:  docker stop test1
# Перевірте контейнери Запущені: docker ps
# Усі: docker ps -a
# Видаліть обидва контейнери:  docker rm test1
# Очистіть докер:  docker system prune

import time
import datetime
import pydantic
import sys

start_program = datetime.datetime.now()

while True:
    time.sleep(2)
    print("Hello!")
    print(f"Version Python: {sys.version}")
    print(f"Version library Pydantic: {pydantic.__version__}")
    print(f"Start program {start_program}\n")
