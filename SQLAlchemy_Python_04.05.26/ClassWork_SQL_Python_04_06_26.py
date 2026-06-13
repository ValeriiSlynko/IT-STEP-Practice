# Параметри підключення до Бази даних
# Краще зберігати в .env
import os

# host = "localhost"  #
# port = 5432         #
# user = "postgres"
# password = "qwerty"
# database = "hospital"

import dotenv
from sqlalchemy import create_engine, text, MetaData
from sqlalchemy.orm import sessionmaker

# читаємо .env
dotenv.load_dotenv()

host = os.getenv("HOST")
port = os.getenv("PORT")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
database = os.getenv("DATABASE")

print(host, port, user, password, database)

# Шлях(uri) до Бази даних
database_uri = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"

# Створення підключення (engine)
engine = create_engine(database_uri)

# Створення сесії(session) на основі підключення(engine)
Session = sessionmaker(bind=engine)
session = Session() # конкретна сесія

# отримання таблиця з Бази даних

metadata = MetaData()
metadata.reflect(bind=engine)

tables = metadata.tables
print(list(tables.keys()))

#Запуск SQL запиту (дані про конкретного  лікаря і т.д.)
query = """
    SELECT *
    FROM DOCTORS
"""

# можно підправити текст
query = text(query)

# запуск
result = session.execute(query)

# виведення результатів
for row in result:
    print(row)
