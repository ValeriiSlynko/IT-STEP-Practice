# Завдання 2
# Для бази даних «Лікарня», яку ви розробляли в рамках
# курсу «Теорія Баз Даних», створіть додаток для взаємодії з базою даних, який дозволяє створювати звіти:
# ▷ Вивести прізвища лікарів та їх спеціалізації;
# ▷ Вивести прізвища та зарплати (сума ставки та надбавки) лікарів, які не перебувають у відпустці;
# ▷ Вивести назви палат, які знаходяться у певному відділенні;
# ▷ Вивести усі пожертвування за вказаний місяць у вигляді:
# відділення, спонсор, сума пожертвування, дата пожертвування;
# ▷ Вивести назви відділень без повторень, які спонсоруються певною компанією.

import os
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

# Шлях(uri) до Бази даних
database_url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"

# Створення підключення (engine)
engine = create_engine(database_url)

# Створення сесії(session) на основі підключення(engine)
Session = sessionmaker(bind=engine)
session = Session() # конкретна сесія

# отримання таблиць з Бази даних
# metadata = MetaData()
# metadata.reflect(bind=engine)

# tables = metadata.tables
# print(list(tables.keys()))

# ---ВИВЕСТИ ПРІЗВИЩА ЛІКАРІВ ТА ЇХ СПЕЦІАЛІЗАЦІЇ ---
# def show_doctors_specializations(session):
#     query = f"""
#         SELECT DOC.SURNAME, SPEC.NAME
#         FROM DOCTORSPECIALIZATIONS DOCSPEC
#             JOIN DOCTORS DOC ON DOCSPEC.DOCTOR_ID = DOC.ID
#             JOIN SPECIALIZATIONS SPEC ON DOCSPEC.SPECIALIZATION_ID = SPEC.ID
# """
#     query = text(query)
#
#     result = session.execute(query)
#     print("\t --doctors surname and specializations--")
#     for row in result:
#         print(row)
#
# # show_doctors_specializations(session)
#
# --- ВИВЕСТИ ПРІЗВИЩА ТА ЗАРПЛАТИ (сума ставки та надбавки) ЛІКАРІВ, ЯКІ НЕ ПЕРЕБУВАЮТЬ У ВІДПУСТЦІ ---
# def show_doctors_salary (session):
#     query = f"""
#         SELECT DOC.SURNAME, DOC.SALARY + DOC.PREMIUM
#         FROM DOCTORS DOC JOIN VACATIONS VAC ON DOC.ID = VAC.DOCTOR_ID
#         WHERE VAC.ENDDATE > CURRENT_DATE AND VAC.STARTDATE < CURRENT_DATE
# """
#     query = text(query)
#
#     result = session.execute(query)
#
#     print("\t --doctors surname and salary--")
#     for row in result:
#         print(row)
#
# show_doctors_specializations(session)
#
# --- ВИВЕСТИ НАЗВИ ПАЛАТ, ЯКІ ЗНАХОДЯТЬСЯ У ПЕВНОМУ ВІДДІЛЕННІ
#
# def _show_name_departments(session):
#     query = f"""
#     SELECT NAME
#     FROM DEPARTMENTS
#
#     """
#     query = text(query)
#     result = session.execute(query)
#     print("\t --departments--")
#     for row in result:
#         print (row)
#
# def show_wards (session):
#     _show_name_departments(session)
#         dep_name = input("Введіть назву відділення")
#
#     query = f"""
#         SELECT *
#         FROM WARDS WAR
#             JOIN DEPARTMENTS DEP ON WAR.DEPARTMENT_ID = DEP.ID
#         WHERE DEP.NAME = '{dep_name}'
# """
#     query = text(query)
#     result = session.execute(query)
#
#     print("\t --doctors surname and salary--")
#     for row in result:
#         print(row)
#
# show_doctors_specializations(session)

# --- ВИВЕСТИ УСІ ПОЖЕРТВУВАННЯ ЗА ВКАЗАНИЙ МІСЯЦЬ У ВИГЛЯДІ:
#   ВІДДІЛЕННЯ, СПОНСОР, СУМА, ПОЖЕРТВУВАННЯ, ДАТА ПОЖЕРТВУВАННЯ, ДАТА ПОЖЕРТВУВАННЯ ---
# def show_donation(session):
#     month_number = input("Введіть місяць (число): ")
#     year_number = input("Введіть рік: ")
#     query = f"""
#         SELECT *
#         FROM DONATIONS DON
#             JOIN DEPARTMENTS DEP ON DON.DEPARTMENT_ID = DEP.ID
#             JOIN SPONSORS SP ON DON.SPONSOR_ID = SP.ID
#         WHERE EXTRACT(MONTH FROM DON.DONATION_DATE) = '{month_number}'
#             AND EXTRACT(YEAR FROM DONATION_DATE) = '{year_number}'
#     """
#     query = text(query)
#     result = session.execute(query)
#
#     for row in result:
#         print(row)
#
# show_donation(session)

# ВИВЕСТИ НАЗВИ ВІДДІЛЕНЬ БЕЗ ПОВТОРЕНЬ, ЯКІ СПОНСОРУЮТЬСЯ ПЕВНОЮ КОМПАНІЄЮ
def show_departments_sponsor(session):
    sponsor_company = input("Enter company name: ")
    query = text("""
        SELECT DISTINCT DEP.NAME, SP.NAME
        FROM DEPARTMENTS DEP JOIN DONATIONS DON ON DON.DEPARTMENT_ID = DEP.ID
            JOIN SPONSORS SP ON DON.SPONSOR_ID = SP.ID
        WHERE SP.NAME = :company_name
    """)

    result = session.execute(query,
                            {"company_name": sponsor_company}
                            )
    for row in result:
        print(row)

show_departments_sponsor(session)
