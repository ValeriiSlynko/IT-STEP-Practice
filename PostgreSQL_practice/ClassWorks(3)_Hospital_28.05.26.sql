-- Таблиці
-- Нижче наведено детальний опис структури кожної таблиці.
-- ¾ Відділення (Departments)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор відділення.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Корпус (Building). Номер корпусу, в якому знаходиться відділення.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Має бути в діапазоні від 1 до 5.
-- ■ Фінансування (Financing). Фонд фінансування відділення.
-- ▷ Тип даних для зберігання грошових значень.
-- ▷ Не містить null-значення.
-- ▷ Не може бути менше, ніж 0.
-- ▷ Значення за замовчуванням — 0.
-- ■ Назва (Name). Назва відділення.
-- ▷ Тип даних — varchar(100).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ▷ Має бути унікальною.


-- CREATE TABLE DEPARTMENT (
--     ID SERIAL PRIMARY KEY,
--     BUILDING INT NOT NULL
--         CHECK (BUILDING > 1 AND BUILDING < 5),
--     FINANCING INT NOT NULL
--         DEFAULT 0
--         CHECK (FINANCING >= 0),
--     NAME VARCHAR(100) NOT NULL
--         UNIQUE
-- );

-- INSERT INTO DEPARTMENT (BUILDING, FINANCING, NAME)
-- VALUES
-- (2, 50000, 'Computer Science'),
-- (3, 75000, 'Mathematics'),
-- (4, 62000, 'Physics'),
-- (2, 45000, 'Biology'),
-- (3, 90000, 'Engineering'),
-- (4, 30000, 'Chemistry'),
-- (2, 55000, 'Economics'),
-- (3, 47000, 'History'),
-- (4, 88000, 'Architecture'),
-- (2, 64000, 'Information Technology');

-- ¾ Захворювання (Diseases)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор
-- захво-рювання.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Назва (Name). Назва захворювання.
-- ▷ Тип даних — varchar(100).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ▷ Має бути унікальною.
-- ■ Ступінь тяжкості (Severity). Ступінь тяжкості захворювання.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Не може бути менше, ніж 1.
-- ▷ Значення за замовчуванням — 1.

-- CREATE TABLE DISEASES (
--     ID SERIAL PRIMARY KEY,
--     NAME VARCHAR(100) NOT NULL
--         UNIQUE
--         CHECK (NAME <> ''),
--     SEVERITY INT NOT NULL
--         DEFAULT 1
--         CHECK (SEVERITY >= 1)
-- );

-- INSERT INTO DISEASES (NAME, SEVERITY)
-- VALUES
-- ('Flu', 2),
-- ('Pneumonia', 4),
-- ('COVID-19', 5),
-- ('Diabetes', 3),
-- ('Hypertension', 2),
-- ('Asthma', 3),
-- ('Migraine', 1),
-- ('Tuberculosis', 5),
-- ('Bronchitis', 2),
-- ('Gastritis', 1);

-- ¾ Лікарі (Doctors)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор
-- лікаря.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Ім’я (Name). Ім’я лікаря.
-- ▷ Тип даних — varchar(255).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожнє.
-- ■ Телефон(Phone). Телефонний номер лікаря.
-- ▷ Тип даних — char(10).
-- ▷ Може містити null-значення.
-- ■ Ставка (Salary). Ставка лікаря.
-- ▷ Тип даних для зберігання грошових значень.
-- ▷ Не містить null-значення.
-- ▷ Не може бути меншою або дорівнювати 0.
-- ■ Прізвище (Surname). Прізвище лікаря.
-- ▷ Тип даних — varchar(255).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожнє.

-- CREATE TABLE DOCTORS (
--     ID SERIAL PRIMARY KEY,
--     NAME VARCHAR(255) NOT NULL
--         CHECK (NAME <> ''),
--     PHONE CHAR(10),
--     SALARY DECIMAL(10,2) NOT NULL
--         CHECK (SALARY > 0),
--     SURNAME VARCHAR(255) NOT NULL
--         CHECK (SURNAME <> '')
-- );

-- INSERT INTO DOCTORS (NAME, PHONE, SALARY, SURNAME)
-- VALUES
-- ('Ivan',      '0671234567', 25000.00, 'Petrenko'),
-- ('Olena',     '0502345678', 32000.50, 'Shevchenko'),
-- ('Andrii',    '0933456789', 28000.75, 'Koval'),
-- ('Maria',     '0664567890', 41000.00, 'Tkachenko'),
-- ('Petro',     '0975678901', 36000.20, 'Bondarenko'),
-- ('Svitlana',  '0686789012', 29500.00, 'Melnyk'),
-- ('Oleh',      '0957890123', 50000.99, 'Boiko'),
-- ('Natalia',   '0638901234', 27000.40, 'Kravchenko'),
-- ('Yurii',     '0999012345', 39000.00, 'Polishchuk'),
-- ('Iryna',     NULL,         33000.00, 'Savchenko');


-- ¾ Обстеження (Examinations)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор обсте-ження.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ День тижня (DayOfWeek). День тижня, коли проводиться обстеження.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Має бути в діапазоні від 1 до 7.
-- ■ Час завершення (EndTime). Час завершення обстеження.
-- ▷ Тип даних для зберігання часу.
-- ▷ Не містить null-значення.
-- ▷ Має бути більше, ніж час початку обстеження.
-- ■ Назва (Name). Назва обстеження.
-- ▷ Тип даних — varchar(100).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ▷ Має бути унікальною.
-- ■ Час початку (StartTime). Час початку обстеження.
-- ▷ Тип даних для зберігання часу.
-- ▷ Не містить null-значення.
-- ▷ Має бути в діапазоні від 8:00 до 18:00.

-- CREATE TABLE EXAMINATIONS (
--     ID SERIAL PRIMARY KEY,
--     DAYOFWEEK INT NOT NULL
--         CHECK (DAYOFWEEK BETWEEN 1 AND 7),
--     STARTTIME TIME NOT NULL
--         CHECK (
--             STARTTIME >= '08:00:00'
--             AND STARTTIME <= '18:00:00'
--         ),
--     ENDTIME TIME NOT NULL
--         CHECK (ENDTIME > STARTTIME),
--     NAME VARCHAR(100) NOT NULL
--         UNIQUE
--         CHECK (NAME <> '')
-- );

-- INSERT INTO EXAMINATIONS
-- (DAYOFWEEK, STARTTIME, ENDTIME, NAME)
-- VALUES
-- (1, '08:30:00', '09:15:00', 'Blood Test'),
-- (2, '09:00:00', '10:00:00', 'MRI Scan'),
-- (3, '10:15:00', '11:00:00', 'Ultrasound'),
-- (4, '11:30:00', '12:10:00', 'X-Ray'),
-- (5, '12:20:00', '13:00:00', 'Cardiogram'),
-- (1, '13:10:00', '14:00:00', 'CT Scan'),
-- (2, '14:15:00', '15:00:00', 'Vision Test'),
-- (3, '15:10:00', '16:00:00', 'Hearing Test'),
-- (4, '16:10:00', '17:00:00', 'Dental Check'),
-- (5, '17:10:00', '17:50:00', 'Heart Examination');

-- ¾ Палати (Wards)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Корпус (Building). Номер корпусу, де знаходиться  палата.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Має бути в діапазоні від 1 до 5.
-- ■ Поверх (Floor). Номер поверху, на якому  знаходиться палата.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Не може бути менше, ніж 1.
-- ■ Назва (Name). Назва палати.
-- ▷ Тип даних — varchar(20).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ▷ Має бути унікальною.

-- CREATE TABLE WARDS (
--     ID SERIAL PRIMARY KEY,
--     BUILDING INT NOT NULL
--         CHECK (BUILDING BETWEEN 1 AND 5),
--     FLOOR INT NOT NULL
--         CHECK (FLOOR >= 1),
--     NAME VARCHAR(20) NOT NULL
--         UNIQUE
--         CHECK (NAME <> '')
-- );

-- INSERT INTO WARDS (BUILDING, FLOOR, NAME)
-- VALUES
-- (1, 1, 'Ward-A101'),
-- (1, 2, 'Ward-A201'),
-- (1, 3, 'Ward-A301'),
-- (2, 1, 'Ward-B101'),
-- (2, 2, 'Ward-B202'),
-- (2, 4, 'Ward-B401'),
-- (3, 1, 'Ward-C103'),
-- (3, 3, 'Ward-C305'),
-- (4, 2, 'Ward-D210'),
-- (5, 5, 'Ward-E505');

-- Завдання 2
-- Для бази даних «Таблиця» створіть такі запити:
-- 1. Вивести вміст таблиці палат.
	-- SELECT *
	-- FROM WARDS

-- 2. Вивести прізвища та телефони усіх лікарів.
	-- SELECT SURNAME, PHONE
	-- FROM DOCTORS

-- 3. Вивести усі поверхи без повторень, де розміщуються палати.
	-- SELECT DISTINCT FLOOR
	-- FROM WARDS
	-- ORDER BY FLOOR

-- 4. Вивести назви захворювань під назвою « Name of Disease» та ступінь їхньої тяжкості під назвою «Severity of Disease».
	-- SELECT NAME AS "Name of Disease", SEVERITY AS "Severity of Disease"
	-- FROM DISEASES;

-- 5. Вивести назви відділень, які знаходяться у корпусі 5 з фондом фінансування меншим, ніж 30000.
	-- SELECT NAME, FINANCING
	-- FROM DEPARTMENT
	-- WHERE BUILDING = 5 AND FINANCING < 30000;

-- 6. Вивести назви відділень, які знаходяться у корпусі 3 з фондом фінансування у діапазоні від 12000 до 15000.
	-- SELECT NAME
	-- FROM DEPARTMENT
	-- WHERE BUILDING = 3 AND FINANCING BETWEEN 12000 AND 15000

-- 8. Вивести назви палат, які знаходяться у корпусах 4 та 5 на 1-му поверсі.
	-- SELECT NAME
	-- FROM WARDS
	-- WHERE BUILDING IN (4, 5) AND FLOOR = 1 ;

-- 9. Вивести назви, корпуси та фонди фінансування відділень, які знаходяться у корпусах 3 або 6 та мають
-- фонд фінансування менший, ніж 11000 або більший за 25000.
	-- SELECT NAME, BUILDING, FINANCING
	-- FROM DEPARTMENT
	-- WHERE BUILDING IN (3, 6) AND (FINANCING < 11000 OR FINANCING > 25000);

-- 10. Вивести прізвища лікарів, зарплата (сума ставки та надбавки 120) яких перевищує 1500.
	-- SELECT NAME, SALARY
	-- FROM DOCTORS
	-- WHERE SALARY + 120 > 1500

-- 11. Вивести прізвища лікарів, у яких половина зарплати перевищує триразову надбавку у вигляді 500.
	-- SELECT SURNAME, SALARY
	-- FROM DOCTORS
	-- WHERE SALARY/2 > 3 * 500;

-- 12. Вивести назви обстежень без повторень, які проводяться у перші три дні тижня з 12:00 до 15:00.
	-- SELECT DISTINCT NAME, STARTTIME, ENDTIME
	-- FROM EXAMINATIONS
	-- WHERE DAYOFWEEK BETWEEN 1 AND 3
	-- 		AND STARTTIME BETWEEN '12:00:00' AND '15:00:00'

-- 13. Вивести назви та номери корпусів відділень, які знаходяться у корпусах 1, 3, 8 або 10.
	-- SELECT NAME, BUILDING
	-- FROM DEPARTMENT
	-- WHERE BUILDING IN (1, 3, 8, 10)

-- 14. Вивести назви захворювань усіх ступенів тяжкості, крім 1-го та 2-го.
	-- SELECT NAME, SEVERITY
	-- FROM DISEASES
	-- WHERE SEVERITY NOT IN (1, 2)

-- 15. Вивести назви відділень, які не знаходяться у першому або третьому корпусі.
	-- SELECT NAME, BUILDING
	-- FROM DEPARTMENT
	-- WHERE BUILDING NOT IN (1, 3)

-- 16. Вивести назви відділень, які знаходяться у першому або третьому корпусі.
	-- SELECT NAME, BUILDING
	-- FROM DEPARTMENT
	-- WHERE BUILDING IN (1, 3)

-- 17. Вивести прізвища лікарів, що починаються з літери «S».
	-- SELECT SURNAME
	-- FROM DOCTORS
	-- WHERE SURNAME ILIKE 'S%'

----- ДОДАТКОВІ ЗАВДАННЯ -----
-- Вивести кількість палат у кожному корпусі.
	-- SELECT BUILDING, COUNT(*) AS WARDS_COUNT
	-- FROM WARDS
	-- GROUP BY BUILDING;

-- Вивести кількість палат на кожному поверсі.
	-- SELECT FLOOR, COUNT(*) AS WARDS_COUNT
	-- FROM WARDS
	-- GROUP BY FLOOR

-- Вивести середній фонд фінансування для кожного корпусу.
	-- SELECT BUILDING, ROUND(AVG(FINANCING),4) AS AVG_FINANSING
	-- FROM DEPARTMENT
	-- GROUP BY BUILDING
	-- ORDER BY AVG_FINANSING DESC

-- Вивести максимальний фонд фінансування серед відділень у кожному корпусі.
	-- SELECT BUILDING, MAX(FINANCING) AS MAX_FINANCING
	-- FROM DEPARTMENT
	-- GROUP BY BUILDING

-- Вивести мінімальний фонд фінансування серед відділень у кожному корпусі.
	-- SELECT BUILDING, MIN(FINANCING) AS MIN_FINANCING
	-- FROM DEPARTMENT
	-- GROUP BY BUILDING

-- Вивести загальну суму фінансування для кожного корпусу.
	-- SELECT BUILDING, SUM(FINANCING) AS SUM_FINANCING
	-- FROM DEPARTMENT
	-- GROUP BY BUILDING
	-- ORDER BY BUILDING ASC

-- Вивести кількість відділень у кожному корпусі.
	-- SELECT BUILDING, COUNT(*) AS DEPARTMENT_COUNT
	-- FROM DEPARTMENT
	-- GROUP BY BUILDING

-- Вивести кількість захворювань для кожного ступеня тяжкості.
	-- SELECT NAME, COUNT(*) AS DISEASES_COUNT
	-- FROM DISEASES
	-- GROUP BY NAME

-- Вивести середню зарплату лікарів залежно від наявності телефону.
	-- SELECT NAME, SURNAME, ROUND(AVG(SALARY),2) AS SALARY_AVG
	-- FROM DOCTORS
	-- WHERE PHONE IS NOT NULL
	-- GROUP BY NAME, SURNAME

-- Вивести середню зарплату лікарів у кожному корпусі.
	-- ВІДСУТНІ ДАНІ ЛІКАРІВ У КОРПУСІ

-- Вивести максимальну зарплату лікарів у кожному корпусі.
	-- ВІДСУТНІ ДАНІ ЗАР.ПЛАТИ ЛІКАРІВ У КОРПУСІ

-- Вивести кількість обстежень для кожного дня тижня.
	-- SELECT  DAYOFWEEK, COUNT(*) AS EXAM_COUNT
	-- FROM EXAMINATIONS
	-- GROUP BY DAYOFWEEK
	-- ORDER BY DAYOFWEEK ASC

-- Вивести найраніший час початку обстежень для кожного дня тижня.
	-- SELECT DAYOFWEEK, MIN(STARTTIME) AS EARLIEST_START
	-- FROM EXAMINATIONS
	-- GROUP BY DAYOFWEEK
	-- ORDER BY DAYOFWEEK ASC

-- Вивести найпізніший час завершення обстежень для кожного дня тижня.
	-- SELECT DAYOFWEEK, MAX(ENDTIME) AS LATELIEST_START
	-- FROM EXAMINATIONS
	-- GROUP BY DAYOFWEEK
	-- ORDER BY DAYOFWEEK ASC

-- Вивести кількість лікарів із зарплатою понад 2000 у кожному корпусі.
	--- ВІДСУТНІ ДАНІ ПРО ЛІКАРІВ, ЗАР.ПЛАТИ У КОРПУСАХ

-- Вивести лікаря, який отримує найБІЛЬШУ зарплату
	-- SELECT NAME, SURNAME, SALARY
	-- FROM DOCTORS
	-- WHERE SALARY = (
	-- 	SELECT MAX(SALARY)
	-- 	FROM DOCTORS
	-- 	)

-- Вивести лікаря, який отримує найМЕНШУ зарплату
	-- SELECT NAME, SURNAME, SALARY
	-- FROM DOCTORS
	-- WHERE SALARY = (
	-- 	SELECT MIN(SALARY)
	-- 	FROM DOCTORS
	-- 	)

-- Вивести лікарів, в яких зарплата вище середньої
	-- SELECT NAME, SURNAME, SALARY
	-- FROM DOCTORS
	-- WHERE SALARY > (
	-- 	SELECT AVG(SALARY)
	-- 	FROM DOCTORS
	-- 	)

--- ДОДАТКОВІ ЗАВДАННЯ (моє виконання) ---

-- SELECT MIN(STARTTIME)
-- FROM EXAMINATIONS

-- Обстеження, яке проводиться найраніше
	-- SELECT *
	-- FROM EXAMINATIONS
	-- WHERE STARTTIME = (
	-- 	SELECT MIN(STARTTIME)
	-- 	FROM EXAMINATIONS
	-- 	)

-- Обстеження, яке проводиться найпізніше
	-- SELECT *
	-- FROM EXAMINATIONS
	-- WHERE ENDTIME = (
	-- 	SELECT MAX(ENDTIME)
	-- 	FROM EXAMINATIONS
	-- 	)
