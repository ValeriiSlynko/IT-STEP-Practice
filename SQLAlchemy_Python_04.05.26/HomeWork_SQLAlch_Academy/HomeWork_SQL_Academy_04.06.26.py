# Курс: «Введення в мову
# програмування Python
# Модуль 18. Використання баз даних
# Тема: Використання баз даних. Частина 2
# ЗАВДАННЯ
# Для бази даних Академія, яку ви розробили в рамках курсу «Теорія Баз Даних»,
# створіть додаток для взаємодії з базою даних, який дозволяє:

# ■ вставляти рядки в таблиці бази даних;
# ■ оновлювати рядків у таблицях бази даних;
# ■ видаляти рядки з таблиць бази даних;
# ■ створювати звіти:
# ▷ вивести інформацію про всі навчальні групи,
# ▷ вивести інформацію про всіх викладачів,
# ▷ вивести назви усіх кафедр,
# ▷ вивести імена та прізвища викладачів, які читають лекції в конкретній групі,
# ▷ вивести назви кафедр і груп, які до них відносяться,
# ▷ відобразити кафедру з максимальною кількістю груп,
# ▷ відобразити кафедру з мінімальною кількістю груп,
# ▷ вивести назви предметів, які викладає конкретний викладач,
# ▷ вивести назви кафедр, на яких викладається конкретна дисципліна,
# ▷ вивести назви груп, що належать до конкретного факультету,
# ▷ вивести назви предметів та повні імена викладачів, які читають найбільшу кількість лекцій з них,
# ▷ вивести назву предмету, за яким читається найменше лекцій,
# ▷ вивести назву предмету, за яким читається найбільше лекцій;
# ■ передбачити можливість збереження звітів з результатів роботи на екран або у файл
    # (встановлюється в налаштуваннях додатку);
# ■ передбачити можливість входу з різними рівнями доступу. Наприклад: доступ лише для читання,
# доступ для читання та запис, доступ для читання певних таблиць.

import os
from idlelib.query import Query
from random import choice

import dotenv
from sqlalchemy import create_engine, text, MetaData
from sqlalchemy.orm import sessionmaker

from lamda import result, surname

# читаємо .env
dotenv.load_dotenv()

host = os.getenv("HOST")
port = os.getenv("PORT")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
database = os.getenv("DATABASE")

# Шлях(uri) до Бази даних
database_uri = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"

# Створення підключення (engine)
engine = create_engine(database_uri)

# Створення сесії(session) на основі підключення(engine)
Session = sessionmaker(bind=engine)
session = Session() # конкретна сесія

# отримання таблиць з Бази даних
metadata = MetaData()       # meta-дані - це дані які десь існують
metadata.reflect(bind=engine)       # meta-дані підключаємо до "engine"

tables = metadata.tables    # словник з таблицями бази даних
print(list(tables.keys()))

# ■ ДОДАТОК вставляє рядки в таблиці бази даних;

def insert_row_menu(session):
    print("ВСТАВЛЕННЯ рядків з даними")
    print("У базі даних 'academy2' доступні таі таблиці: FACULTIES, DEPARTMENTS, GROUPS, CURATORS, SUBJECTS, TEACHERS")
    table = input("Введіть назву таблиці(з доступних) для додавання запису: ").strip().lower()

    if table == "faculties":
        name = input("Введіть назву факультету: ")
        query = text("INSERT INTO FACULTIES (name) VALUES (:name)")
        session.execute(query, {"name": name})

    elif table == "departments":
        name = input("Введіть назву кафедри: ")
        financing = input("Введіть фінінсування(число): ")
        faculty_id = input("Введіть ID факультету: ")
        query = text("INSERT INTO DEPARTMENTS (name, financing, faculty_ID) VALUES (:name, :financing, :faculty_id)")
        session.execute(query, {"name":name, "financing":financing, "faculty_id":faculty_id})

    elif table == "groups":
        name = input("Введіть назву групи: ")
        year = input("Введіть курс (від 1 до 5): ")
        department_id = input("Введіть ID кафедри: ")
        query = text("INSERT INTO GROUPS (name, year, department_id) VALUES (:name, :year, :department_id)")
        session.execute(query, {"name":name, "year":year, "department_id":department_id})

    elif table == "teachers":
        name = input("Введіть ім'я викладача: ")
        surname = input("Введіть прізвище  викладача: ")
        salary = input("Введіть зар.плату: )")
        query = text("INSERT INTO TEACHERS (name, surname, salary) VALUES (:name, :surname, :salary)")
        session.execute(query, {"name":name, "surname":surname, "salary":salary})

    elif table == "subjects":
        name = input("Введіть назву предмета: ")
        query = text("INSERT INTO SUBJECTS (name) VALUES (:name)")
        session.execute(query, {"name":name})

    else:
        print("Таблицю не знайдено або додавання рядків з даними не налаштовано!")
        return

    session.commit()
    print(f"Запис успішно додано в таблицю: '{table}'")

# ■ ДОДАТОК оновлює рядки у таблицях бази даних;

def update_row_menu(session):
    print("\nОНОВЛЕННЯ рядків з даними!")
    print("Оберіть, що потрібно оновити: ")
    print("-1- Змінити фінінсування кафедри")
    print("-2- Змінити курс групи")
    print("-3- Змінити зар.плату викладача")
    choice = input("Зробіть вибір (від 1 до 3): ").strip().lower()

    if choice == "-1":
        dep_id = input("Введіть ID кафедри: ")
        new_fin = input("Введіть зміни у фінансуванні: ")
        query = text("UPDATE departments SET financing = :financing WHERE id = :id")
        session.execute(query, {"id":dep_id, "financing":new_fin})

    elif choice == "-2":
        group_id = input("Введіть ID групи: ")
        new_name = input("Введіть нову назву групи: ")
        new_year = input("Введіть новий курс групи (від 1 до 5): ")
        query = text("UPDATE groups SET name = :name, year = :year WHERE id = :id")
        session.execute(query, {"name": new_name, "year": new_year, "id": group_id})

    elif choice == "-3":
        teacher_id = input("Введіть ID викладача: ")
        new_salary = input("Введіть нову зарплату: ")
        query = text("UPDATE teachers SET salary = :salary WHERE id = :id")
        session.execute(query, {"id": teacher_id, "salary": new_salary})

    else:
        print("Неправильний вибір.")
        return

    session.commit()
    print("Дані успішно оновлено!")

# ■ ДОДАТОК видаляє рядки з таблиць бази даних;

def delete_row_menu(session):
    print("\nВИДАЛЕННЯ рядків з таблиць бази даних!")
    print("Доступні таблиці для видалення: faculties, departments, groups, teachers, subjects")
    table = input("З якої таблиці видалити запис?: ").strip().lower()
    row_id = input("Введіть ID запису, який потрібно видалити: ")

    # Перевіряємо назву таблиці, щоб уникнути SQL-ін'єкцій
    valid_tables = ["FACULTIES", "DEPARTMENTS", "GROUPS", "TEACHERS", "SUBJECTS"]
    if table not in valid_tables:
        print("Неприпустима назва таблиці.")
        return

    # Динамічно підставляємо назву таблиці безпечним шляхом
    query = text(f"DELETE FROM {table} WHERE id = :id")

    try:
        session.execute(query, {"id": row_id})
        session.commit()
        print(f"Запис з ID {row_id} успішно видалено з таблиці '{table}'!")
    except Exception as exp:
        session.rollback()  # Скасовуємо зміни у разі помилки зв'язків (Foreign Key)
        print(f"Помилка видалення: можливо, цей запис використовується в інших таблицях.")


if __name__ == "__main__":
    # Тестуємо вставлення рядків БД
    insert_row_menu(session)

    # Тестуємо оновлення рядків БД
    # update_row_menu(session)

    # Тестуємо видалення рядків БД
    # delete_row_menu(session)

# ■ СТВОРЮЄМО ЗВІТИ:
# ▷ вивести інформацію про всі навчальні групи
def info_all_groups(session):
    print("\n ІНФОРМАЦІЯ ПРО ВСІ НАВЧАЛЬНІ ГРУПИ")

    query = """
            SELECT id, name, year, department_id
            FROM GROUPS
            """
    query = text(query)
    result = session.execute(query)
    for row in result:
        print(f"id: {row.id}, name: {row.name}, year: {row.year}, department_id: {row.department_id}")

# ▷ вивести інформацію про всіх викладачів
def info_all_teachers(session):
    print("\n ІНФОРМАЦІЯ ПРО ВСІХ ВИКЛАДАЧІВ")

    query = text("""
                SELECT ID, NAME, SURNAME, SALARY
                FROM TEACHERS
                """)
    result = session.execute(query)
    for row in result:
        print(f"id: {row.id}, name: {row.name}, surname: {row.surname}")

# ▷ вивести назви усіх кафедр
def info_all_departments(session):
    print("\n ВИВОДИМО НАЗВИ УСІХ КАФЕДР")

    query = text("""
                SELECT ID, NAME
                FROM DEPARTMENTS
                """)
    result = session.execute(query)
    for row in result:
        print(f"id: {row.id}, name: {row.name}")

# ▷ вивести імена та прізвища викладачів, які читають лекції в конкретній групі,
def info_teachers_group(session):
    print("\n ВИВОДИМО ІМЕНА та ПРІЗВИЩА ВИКЛАДАЧІВ КОНКРЕТНОЇ ГРУПИ")
    group_name = input("Введіть назву групи: ").strip()

    query = text("""
                SELECT DISTINCT TCH.NAME, TCH.SURNAME
                FROM TEACHERS TCH
                    JOIN LECTURES LEC ON LEC.TEACHER_ID = THC.ID
                    JOIN GROUPS_LECTURES GRL ON GRL.LECTURE_ID = LEC.ID
                    JOIN GROUPS GR ON GRL.GROUP_ID = GR.ID
                    WHERE GR.NAME = :GROUP_NAME
                """)
    result = session.execute(query, {group_name: group_name})
    for row in result:
        print(f"id: {row.id}, name: {row.name}, surname: {row.surname}")

# ▷ вивести назви кафедр і груп, які до них відносяться,
def info_name_departments(session):
    print("\n ВИВОДИМО НАЗВИ КАФЕДР і ГРУП")
    departments_name = input("Введіть назву групи: ").strip()

    query = text("""
                SELECT DEP.NAME as DEPARTMENT_NAME, GR.NAME as GROUP_NAME
                FROM DEPARTMENTS DEP JOIN GROUPS GR ON DEP.ID = GR.DEPARTMENT_ID
                """)
    result = session.execute(query)
    for row in result:
        print(f"Кафедра: {row.department_id} | Група: {row.group_name}")

# ▷ відобразити кафедру з максимальною кількістю груп,
def info_max_group_department(session):
    print("ВИВОДИМО КАФЕДРУ З МАКСИМАЛЬНОЮ КІЛЬКІСТЮ ГРУП")

    query = text("""
                SELECT DEP.NAME as DEPARTMENT_NAME, COUNT (GR.ID) as COUNT_GROUPS
                FROM DEPARTMENTS DEP
                    LEFT JOIN GROUPS GR ON DEP.ID = GR.DEPARTMENT_ID
                GROUP BY DEP.ID, DEP.NAME
                ORDER BY COUNT_GROUPS DESC
                LIMIT 1
                """)
    result = session.execute(query)
    for row in result:
        print(f"Кафедра: {row.name} | Кількість груп: {row.count_groups}")

# ▷ відобразити кафедру з мінімальною кількістю груп,
def info_max_group_departments(session):
    print("ВИВОДИМО КАФЕДРУ З МІНІМАЛЬНОЮ КІЛЬКІСТЮ ГРУП")

    query = text("""
                SELECT DEP.NAME as DEPARTMENT_NAME, COUNT (GR.ID) as COUNT_GROUPS
                FROM DEPARTMENTS DEP
                    LEFT JOIN GROUPS GR ON DEP.ID = GR.DEPARTMENT_ID
                GROUP BY DEP.ID, DEP.NAME
                ORDER BY COUNT_GROUPS ASC
                LIMIT 1
                """)
    result = session.execute(query)
    for row in result:
        print(f"Кафедра: {row.name} | Кількість груп: {row.count_groups}")

# ▷ вивести назви предметів, які викладає конкретний викладач,
def info_subject_by_teachers(session):
    print("ВИВОДИМО НАЗВУ ПРЕДМЕТІВ ЯКІ ВИКЛАДАЄ КОНКРЕТНИЙ ВИКЛАДАЧ")
    teacher_surname = input("Введіть прізвище викладача: ").strip()

    query = text("""
            SELECT SUB.NAME as SUBJECT_NAME,
            FROM SUBJECT SUB JOIN LECTURES LEC ON SUB.ID = LEC.SUBJECT_ID
                JOIN TEACHERS TCH ON TCH.ID = LEC.TEACHER_ID
            WHERE TCH.SURNAME = :SURNAME
            """)
    result = session.execute(query, {"surname": surname})
    rows = result.all()
    if not rows:
        print(f"Предметів для викладача- {teacher_surname} не знайдено")
    for row in result:
        print(f"Назви предметів: {row.name} які викладає: {teacher_surname}")

# ▷ вивести назви кафедр, на яких викладається конкретна дисципліна,
def info_departments_by_subject(session):
    print("\n НАЗВИ КАФЕДР, НА ЯКИХ ВИКЛАДАЄТЬСЯ ДИСЦИПЛІНА")
    subject_name = input("Введіть назву предмета: ").strip()

    query = text("""
        SELECT DISTINCT d.name
        FROM DEPARTMENTS DEP JOIN GROUPS GR ON GR.DEPARTMENT_ID = DEP.ID
            JOIN GROUPS_LECTURES GL ON GL.GROUP_ID = GR.id
            JOIN LECTURES LEC ON GL.LECTURE_ID = LEC.ID
            JOIN SUBJECTS SUB ON LEC.SUBJECT_ID = SUB.ID
        WHERE SUB.NAME = :SUBJECT_NAME
    """)
    result = session.execute(query, {"subject_name": subject_name})
    rows = result.all()
    if not rows:
        print(f"Кафедр для предмета {subject_name} не знайдено.")
    for row in rows:
        print(f"Кафедра: {row.name}")

# ▷ вивести назви груп, що належать до конкретного факультету,
def info_groups_by_faculty(session):
    print("\n НАЗВИ ГРУП, ЩО НАЛЕЖАТЬ ДО КОНКРЕТНОГО ФАКУЛЬТЕТУ")
    faculty_name = input("Введіть назву факультету: ").strip()

    query = text("""
        SELECT GR.NAME
        FROM GROUPS GR JOIN DEPARTMENTS DEP ON GR.DEPARTMENT_ID = DEP.ID
            JOIN FACULTIES FAC ON DEP.FACULTY_ID = FAC.ID
        WHERE FAC.NAME = :FACULTY_NAME
    """)
    result = session.execute(query, {"faculty_name": faculty_name})
    rows = result.all()
    if not rows:
        print(f"Груп для факультету {faculty_name} не знайдено.")
    for row in rows:
        print(f"Група: {row.name}")

# ▷ вивести назви предметів та повні імена викладачів, які читають найбільшу кількість лекцій з них
def info_top_lectures_by_subject(session):
    print("\n ЛІДЕРИ ЗА КІЛЬКІСТЮ ЛЕКЦІЙ З ПРЕДМЕТІВ")

    query = text("""
        SELECT sub.name AS sub_name, tch.name AS t_name, tch.surname AS t_surname, COUNT(lec.id) AS count_lectures
        FROM subjects sub JOIN lectures lec ON lec.subject_id = sub.id
            JOIN teachers tch ON lec.teacher_id = tch.id
        GROUP BY sub.id, sub.name, tch.id, tch.name, tch.surname
        ORDER BY count_lectures DESC
    """)
    result = session.execute(query)
    for row in result:
        print(f"Предмет: {row.sub_name} | Викладач: {row.t_name} {row.t_surname} | Лекцій: {row.count_lectures}")

# ▷ вивести назву предмета, за яким читається найменше лекцій
def info_min_lectures_subject(session):
    print("\n ПРЕДМЕТ З НАЙМЕНШОЮ КІЛЬКІСТЮ ЛЕКЦІЙ")

    query = text("""
        SELECT sub.name, COUNT(l.id) AS count_lectures
        FROM subjects sub
            LEFT JOIN lectures lec ON lec.subject_id = sub.id
        GROUP BY sub.id, sub.name
        ORDER BY count_lectures ASC
        LIMIT 1
    """)
    row = session.execute(query).first()
    if row:
        print(f"Предмет: {row.name} | Лекцій: {row.count_lectures}")

# ▷ вивести назву предмета, за яким читається найбільше лекцій;
def info_max_lectures_subject(session):
    print("\n ПРЕДМЕТ З МАКСИМАЛЬНОЮ КІЛЬКІСТЮ ЛЕКЦІЙ")

    query = text("""
        SELECT sub.name, COUNT(lec.id) AS count_lectures
        FROM subjects sub
        LEFT JOIN lectures lec ON lec.subject_id = sub.id
        GROUP BY sub.id, sub.name
        ORDER BY count_lectures DESC
        LIMIT 1
    """)
    row = session.execute(query).first()
    if row:
        print(f"Предмет: {row.name} | Лекцій: {row.count_lectures}")


# ■ передбачити можливість збереження звітів з результатів роботи на екран або у файл
    # (встановлюється в налаштуваннях додатка);
#       --- ДОПОМОГА ШІ! ---

# 1. СТВОРЮЄМО ЗМІННУ НАЛАШТУВАНЬ (False - екран, True - файл)
SAVE_TO_FILE = False

# 2. ФУНКЦІЯ ДЛЯ ЗМІНИ НАЛАШТУВАНЬ В МЕНЮ
def change_settings():
    global SAVE_TO_FILE

    print("\nНАЛАШТУВАННЯ ДОДАТКА:")
    print("1. Виводити звіти на екран")
    print("2. Зберігати звіти у файл 'report.txt'")

    choice = input("Оберіть режим (1 або 2): ").strip()

    if choice == "1":
        SAVE_TO_FILE = False
        print("Звіти будуть виводитися на екран.")
    elif choice == "2":
        SAVE_TO_FILE = True
        print("Звіти будуть зберігатися у файл report.txt.")

# 3. ВАШЕ ГОЛОВНЕ МЕНЮ (приклад, як туди додати налаштування)

def main_menu(session):
    while True:
        print("\n--- ГОЛОВНЕ МЕНЮ ---")
        print("1. Звіт про групи")
        print("2. Звіт про кафедри і групи")
        print("3. НАЛАШТУВАННЯ (Екран / Файл)")  # Додали новий пункт!
        print("0. Вихід")

        choice = input("Ваш вибір: ").strip()

        if choice == "1":
            info_all_groups(session)
        elif choice == "2":
            info_name_departments(session)
        elif choice == "3":
            change_settings()  # Викликаємо нашу функцію налаштувань!
        elif choice == "0":
            print("Вихід з програми...")
            break

# ■ передбачити можливість входу з різними рівнями доступу.
# Наприклад: доступ лише для читання, доступ для читання та запис, доступ для читання певних таблиць.
#       --- ДОПОМОГА ШІ! ---

# Початкове налаштування: False означає, що користувач — Гість (тільки читання).
# True означає, що користувач — Адмін (повний доступ).
IS_ADMIN = False

def login_system():
    global IS_ADMIN  # Кажемо Python, що будемо міняти нашу змінну з Кроку 1

    print("\n ВХІД У СИСТЕМУ «АКАДЕМІЯ»")
    print("1. Увійти як Гість (Тільки перегляд звітів)")
    print("2. Увійти як Адміністратор (Повний доступ)")

    choice = input("Оберіть варіант (1 або 2): ").strip()

    if choice == "2":
        password = input("Введіть пароль адміністратора: ").strip()
        if password == "123":  # Простий пароль
            IS_ADMIN = True
            print("Успішно! Ви увійшли як -АДМІНІСТРАТОР.")
        else:
            IS_ADMIN = False
            print("Невірний пароль! Для вас увімкнено режим -ГІСТЬ.")
    else:
        IS_ADMIN = False
        print("Ви увійшли як ГІСТЬ.")
