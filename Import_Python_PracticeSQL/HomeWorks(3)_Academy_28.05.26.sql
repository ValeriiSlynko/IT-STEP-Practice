-- Курс: «Введення в мову
-- програмування Python
-- Модуль 15. Вступ до теорії баз даних
-- Тема: Вступ до теорії баз даних.
-- Частина 3
-- Завдання 1
-- Створіть базу даних Академія (Academy), яка міститиме
-- інформацію про співробітників та внутрішній порядок академії.
-- Опис бази даних знаходиться в кінці файлу.

-- Таблиці
-- Нижче наведено опис структури кожної таблиці.
-- ¾ Кафедри (Departments)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор кафедри.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Фінансування (Financing). Фонд фінансування кафедри.
-- ▷ Тип даних — money.
-- ▷ Не містить null-значення.
-- ▷ Не може бути менше, ніж 0.
-- ▷ Значення за замовчуванням — 0.
-- ■ Назва (Name). Назва кафедри.
-- ▷ Тип даних — varchar(100).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ▷ Має бути унікальною.
	-- CREATE TABLE DEPARTMENTS (
	-- 	ID SERIAL PRIMARY KEY,
	-- 	FINANCING MONEY NOT NULL
	-- 		DEFAULT 0
	-- 		CHECK (FINANCING >= 0::money),
	-- 	NAME VARCHAR(100) NOT NULL
	-- 		CHECK (NAME <> '')
	-- 		UNIQUE
	-- )

	-- INSERT INTO DEPARTMENTS (FINANCING, NAME)
	-- VALUES
	-- (150000::money, 'Computer Science'),
	-- (120000::money, 'Mathematics'),
	-- (98000::money, 'Physics'),
	-- (87000::money, 'Chemistry'),
	-- (76000::money, 'Biology'),
	-- (134000::money, 'Economics'),
	-- (92000::money, 'History'),
	-- (81000::money, 'Philosophy'),
	-- (143000::money, 'Engineering'),
	-- (99000::money, 'Architecture'),
	-- (111000::money, 'Medicine'),
	-- (67000::money, 'Psychology'),
	-- (89000::money, 'Sociology'),
	-- (73000::money, 'Political Science'),
	-- (158000::money, 'Artificial Intelligence'),
	-- (140000::money, 'Cybersecurity'),
	-- (125000::money, 'Data Analytics'),
	-- (95000::money, 'Journalism'),
	-- (102000::money, 'Law'),
	-- (85000::money, 'Linguistics');

-- ¾ Факультети(Faculties)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор факультету.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Декан (Dean). Декан факультету.
-- ▷ Тип даних — varchar(255).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожнім.
-- ■ Назва (Name). Назва факультету.
-- ▷ Тип даних — varchar(100).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ▷ Має бути унікальною.
	-- CREATE TABLE FACULTIES (
	-- 	ID SERIAL PRIMARY KEY,
	-- 	DEAN VARCHAR(255) NOT NULL
	-- 		CHECK (DEAN <> ''),
	-- 	NAME VARCHAR(100) NOT NULL
	-- 		CHECK (NAME <> '')
	-- 		UNIQUE
	-- )
	-- INSERT INTO FACULTIES (DEAN, NAME)
	-- VALUES
	-- ('John Smith', 'Faculty of Computer Science'),
	-- ('Emily Johnson', 'Faculty of Engineering'),
	-- ('Michael Brown', 'Faculty of Medicine'),
	-- ('Sarah Davis', 'Faculty of Economics'),
	-- ('David Wilson', 'Faculty of Law'),
	-- ('Olivia Taylor', 'Faculty of Physics'),
	-- ('Daniel Anderson', 'Faculty of Mathematics'),
	-- ('Sophia Martinez', 'Faculty of Biology'),
	-- ('James Thomas', 'Faculty of History'),
	-- ('Emma White', 'Faculty of Psychology');

-- ¾ Групи (Groups)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор групи.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Назва (Name). Назва групи.
-- ▷ Тип даних — varchar(10).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ▷ Має бути унікальною.
-- ■ Рейтинг (Rating). Рейтинг групи.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Має бути в діапазоні від 0 до 5.
-- ■ Курс (Year). Курс (рік), на якому навчається група.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Має бути в діапазоні від 1 до 5.
	-- CREATE TABLE GROUPS (
	-- ID SERIAL PRIMARY KEY,
	-- NAME VARCHAR(10) NOT NULL
	-- 	CHECK (NAME <> '')
	-- 	UNIQUE,
	-- RATING INT NOT NULL
	-- 	CHECK (RATING BETWEEN 0 AND 5),
	-- YEAR INT NOT NULL
	-- 	CHECK (YEAR BETWEEN 1 AND 5)
	-- )

	-- INSERT INTO GROUPS (NAME, RATING, YEAR)
	-- VALUES
	-- ('CS101', 5, 1),
	-- ('CS102', 4, 1),
	-- ('CS201', 3, 2),
	-- ('CS202', 5, 2),
	-- ('CS301', 4, 3),
	-- ('CS302', 2, 3),
	-- ('CS401', 5, 4),
	-- ('CS402', 3, 4),
	-- ('CS501', 4, 5),
	-- ('CS502', 5, 5),

	-- ('ENG101', 2, 1),
	-- ('ENG102', 3, 1),
	-- ('ENG201', 4, 2),
	-- ('ENG202', 5, 2),
	-- ('ENG301', 3, 3),
	-- ('ENG302', 2, 3),
	-- ('ENG401', 5, 4),
	-- ('ENG402', 4, 4),
	-- ('ENG501', 5, 5),
	-- ('ENG502', 3, 5),

	-- ('MED101', 4, 1),
	-- ('MED102', 5, 1),
	-- ('MED201', 2, 2),
	-- ('MED202', 3, 2),
	-- ('MED301', 5, 3),
	-- ('MED302', 4, 3),
	-- ('MED401', 5, 4),
	-- ('MED402', 3, 4),
	-- ('MED501', 4, 5),
	-- ('MED502', 5, 5),

	-- ('LAW101', 3, 1),
	-- ('LAW102', 4, 1),
	-- ('LAW201', 5, 2),
	-- ('LAW202', 2, 2),
	-- ('LAW301', 4, 3),
	-- ('LAW302', 5, 3),
	-- ('LAW401', 3, 4),
	-- ('LAW402', 4, 4),
	-- ('LAW501', 5, 5),
	-- ('LAW502', 2, 5),

	-- ('BIO101', 4, 1),
	-- ('BIO102', 3, 1),
	-- ('BIO201', 5, 2),
	-- ('BIO202', 4, 2),
	-- ('BIO301', 2, 3),
	-- ('BIO302', 3, 3),
	-- ('BIO401', 5, 4),
	-- ('BIO402', 4, 4),
	-- ('BIO501', 5, 5),
	-- ('BIO502', 3, 5);

-- ¾ Викладачі(Teachers)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор
-- викладача.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Дата працевлаштування (EmploymentDate). Дата працевлаштування викладача.
-- ▷ Тип даних — date.
-- ▷ Не містить null-значення.
-- ▷ Не може бути менше 01.01.1990.
-- ■ Асистент (IsAssistant). Чи є викладач асистентом.
-- ▷ Тип даних — bit.
-- ▷ Не містить null-значення.
-- ▷ Значення за замовчуванням — 0.
-- ■ Професор (IsProfessor). Чи є викладач професором.
-- ▷ Тип даних — bit.
-- ▷ Не містить null-значення.
-- ▷ Значення за замовчуванням — 0.
-- ■ Ім’я (Name). Ім’я викладача.
-- ▷ Тип даних — nvarchar(max).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожнє.
-- ■ Посада (Position). Посада викладача.
-- ▷ Тип даних — varchar(max).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ■ Надбавка (Premium). Надбавка викладача.
-- ▷ Тип даних — money.
-- ▷ Не містить null-значення.
-- ▷ Не може бути менше, ніж 0.
-- ▷ Значення за замовчуванням — 0.
-- ■ Ставка (Salary). Ставка викладача.
-- ▷ Тип даних — money.
-- ▷ Не містить null-значення.
-- ▷ Не може бути меншою або дорівнювати 0.
-- ■ Прізвище (Surname). Прізвище викладача.
-- ▷ Тип даних — varchar(max).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожнє.
	-- CREATE TABLE TEACHERS (
	-- ID SERIAL PRIMARY KEY,
	-- EMPLOYMENT_DATE DATE NOT NULL
	-- 	CHECK (EMPLOYMENT_DATE >= '1990-01-01'),
	-- IS_ASSISTANT BIT(1) NOT NULL
	-- 	DEFAULT B'0',
	-- IS_PROFESSOR BIT(1) NOT NULL
	-- 	DEFAULT B'0',
	-- NAME VARCHAR(100) NOT NULL
	-- 	CHECK (NAME <> ''),
	-- POSITION VARCHAR(100) NOT NULL
	-- 	CHECK (POSITION <> ''),
	-- PREMIUM MONEY NOT NULL
	-- 	CHECK (PREMIUM >= 0::MONEY)
	-- 	DEFAULT 0,
	-- SALARY MONEY NOT NULL
	-- 	CHECK (SALARY > 0::MONEY),
	-- SURNAME VARCHAR(100) NOT NULL
	-- 	CHECK (SURNAME <> '')
	-- )

	-- 	INSERT INTO TEACHERS
	-- (EMPLOYMENT_DATE, IS_ASSISTANT, IS_PROFESSOR, NAME, POSITION, PREMIUM, SALARY, SURNAME)
	-- VALUES
	-- ('1995-03-12', B'1', B'0', 'John', 'Lecturer', 500::money, 3000::money, 'Smith'),
	-- ('2001-07-22', B'0', B'1', 'Emily', 'Professor', 1200::money, 6000::money, 'Johnson'),
	-- ('1998-11-10', B'1', B'0', 'Michael', 'Assistant', 300::money, 2500::money, 'Brown'),
	-- ('2005-09-01', B'0', B'0', 'Sarah', 'Lecturer', 450::money, 3200::money, 'Davis'),
	-- ('1992-04-18', B'0', B'1', 'David', 'Professor', 1500::money, 7000::money, 'Wilson'),
	-- ('1999-06-25', B'1', B'0', 'Olivia', 'Assistant', 350::money, 2700::money, 'Taylor'),
	-- ('2008-01-15', B'0', B'0', 'Daniel', 'Lecturer', 400::money, 3100::money, 'Anderson'),
	-- ('1993-12-20', B'0', B'1', 'Sophia', 'Professor', 1800::money, 7500::money, 'Martinez'),
	-- ('2000-05-30', B'1', B'0', 'James', 'Assistant', 250::money, 2400::money, 'Thomas'),
	-- ('2010-08-11', B'0', B'0', 'Emma', 'Lecturer', 500::money, 3300::money, 'White'),

	-- ('1997-02-14', B'1', B'0', 'Liam', 'Assistant', 350::money, 2600::money, 'Harris'),
	-- ('1991-10-05', B'0', B'1', 'Noah', 'Professor', 2000::money, 8000::money, 'Martin'),
	-- ('2003-03-19', B'0', B'0', 'Ava', 'Lecturer', 600::money, 3400::money, 'Thompson'),
	-- ('1996-06-08', B'1', B'0', 'Ethan', 'Assistant', 300::money, 2500::money, 'Garcia'),
	-- ('2007-09-27', B'0', B'0', 'Mia', 'Lecturer', 450::money, 3200::money, 'Robinson'),

	-- ('1994-11-13', B'0', B'1', 'Lucas', 'Professor', 1700::money, 7200::money, 'Clark'),
	-- ('2002-04-09', B'1', B'0', 'Charlotte', 'Assistant', 280::money, 2450::money, 'Rodriguez'),
	-- ('1990-01-17', B'0', B'1', 'Benjamin', 'Professor', 2200::money, 8500::money, 'Lewis'),
	-- ('2012-05-22', B'0', B'0', 'Amelia', 'Lecturer', 500::money, 3350::money, 'Lee'),
	-- ('2006-12-03', B'1', B'0', 'Henry', 'Assistant', 320::money, 2550::money, 'Walker'),

	-- ('1998-08-16', B'0', B'0', 'Evelyn', 'Lecturer', 470::money, 3250::money, 'Hall'),
	-- ('1993-01-29', B'0', B'1', 'Alexander', 'Professor', 1900::money, 7700::money, 'Allen'),
	-- ('2004-06-11', B'1', B'0', 'Harper', 'Assistant', 310::money, 2480::money, 'Young'),
	-- ('1999-09-09', B'0', B'0', 'Sebastian', 'Lecturer', 520::money, 3450::money, 'Hernandez'),
	-- ('2001-02-25', B'1', B'0', 'Abigail', 'Assistant', 290::money, 2430::money, 'King'),

	-- ('1995-07-07', B'0', B'1', 'Matthew', 'Professor', 2100::money, 8100::money, 'Wright'),
	-- ('2009-10-14', B'0', B'0', 'Ella', 'Lecturer', 480::money, 3280::money, 'Lopez'),
	-- ('1997-05-19', B'1', B'0', 'Jackson', 'Assistant', 330::money, 2590::money, 'Hill'),
	-- ('1992-03-28', B'0', B'1', 'Scarlett', 'Professor', 1750::money, 7300::money, 'Scott'),
	-- ('2011-11-30', B'0', B'0', 'Aiden', 'Lecturer', 510::money, 3380::money, 'Green');

-- Завдання 2
-- Для бази даних Академія створіть такі запити:
-- 1. Вивести таблицю кафедр, але розташувати її поля у зворотному порядку.
	SELECT NAME, FINANCING, ID
	FROM DEPARTMENTS

-- 2. Вивести назви груп та їх рейтинги з уточненнями до назв полів відповідно до назви таблиці.
	SELECT NAME AS GROUP_NAME, RATING AS RATING_NAME
	FROM GROUPS
	ORDER BY RATING_NAME DESC

-- 3. Вивести для викладачів їх прізвища, відсоток ставки по відношенню до надбавки
	--та відсоток ставки по відношенню до зарплати (сума ставки та надбавки).
	SELECT NAME||' '||SURNAME,
		ROUND((SALARY::NUMERIC / NULLIF(PREMIUM::NUMERIC,0) * 100),2) AS SAL_TO_PREM_PERC,
		ROUND((SALARY::	NUMERIC / NULLIF((SALARY::NUMERIC + PREMIUM::NUMERIC),0) * 100),2) AS SAL_TOTAL_PERCENT
	FROM TEACHERS

-- 4. Вивести таблицю факультетів одним полем у такому форматі: «The dean of faculty [faculty] is [dean].».
	SELECT '"'||'The dean of faculty'||' '|| '['||NAME||']'||' is '||'['||DEAN||']'||'.' AS INFO_DEAN_FACULTY
	FROM FACULTIES

-- 5. Вивести прізвища професорів, ставка яких перевищує 1050.
	SELECT SURNAME, SALARY
	FROM TEACHERS
	WHERE IS_PROFESSOR = B'1' AND SALARY::NUMERIC > 1050

-- 6. Вивести назви кафедр, фонд фінансування яких менший, ніж 11000 або більший за 25000.
	SELECT NAME, FINANCING
	FROM DEPARTMENTS
	WHERE FINANCING::NUMERIC < 11000 OR FINANCING::NUMERIC > 25000

-- 7. Вивести назви факультетів, окрім факультету «ComputerScience».
	SELECT NAME
	FROM FACULTIES
	WHERE NAME != 'Faculty of Computer Science'

-- 8. Вивести прізвища та посади викладачів, які не є професорами.
	SELECT SURNAME, POSITION
	FROM TEACHERS
	WHERE IS_PROFESSOR = B'0'

-- 9. Вивести прізвища, посади, ставки та надбавки асистентів, надбавка яких у діапазоні від 160 до 550.
	SELECT SURNAME, POSITION, SALARY, PREMIUM
	FROM TEACHERS
	WHERE IS_ASSISTANT = B'1' AND PREMIUM::NUMERIC BETWEEN 160 AND 550

-- 10. Вивести прізвища та ставки асистентів.
	SELECT SURNAME, SALARY
	FROM TEACHERS
	WHERE IS_ASSISTANT = B'1'

-- 11. Вивести прізвища та посади викладачів, які були прийняті на роботу до 01.01.2000.
	SELECT SURNAME, POSITION, EMPLOYMENT_DATE
	FROM TEACHERS
	WHERE EMPLOYMENT_DATE < '2000-01-01'

-- 12. Вивести назви кафедр, які в алфавітному порядку розміщені до кафедри «Software Development».
	-- Виведене поле назвіть «Name of Department».
INSERT INTO DEPARTMENTS (FINANCING, NAME)
VALUES (130000::MONEY, 'Software Development')

	SELECT NAME AS "Name of Department"
	FROM DEPARTMENTS
	WHERE NAME < 'Software Development'

-- 13. Вивести прізвища асистентів із зарплатою (сума ставки та надбавки) не більше 1200.
	SELECT SURNAME, SALARY
	FROM TEACHERS
	WHERE SALARY::NUMERIC + PREMIUM::NUMERIC <= 1200

-- 14. Вивести назви груп 5-го курсу з рейтингом у діапазоні від 2 до 4.
	SELECT NAME, YEAR, RATING
	FROM GROUPS
	WHERE YEAR = 5 AND RATING BETWEEN 2 AND 4
	ORDER BY RATING DESC

-- 15. Вивести прізвища асистентів зі ставкою менше, ніж 550 або надбавкою менше, ніж 2000.
	SELECT SURNAME, SALARY, PREMIUM
	FROM TEACHERS
	WHERE IS_ASSISTANT = B'1' AND (SALARY::NUMERIC < 550 OR PREMIUM::NUMERIC < 2000)
