-- Курс: «Введення в мову
-- програмування Python
-- Модуль 15. Вступ до теорії баз даних
-- Тема: Вступ до теорії баз даних.

-- Частина 1
-- ЗАВДАННЯ 1
-- Створіть базу даних під назвою Sample. Розташування файлів залишається на ваш вибір.
--РІШЕННЯ:
  -- CREATE DATABASE SAMPLE;

-- ЗАВДАННЯ 2
-- Переназвіть базу даних із першого завдання. Нове ім’я для бази даних Example.
--РІШЕННЯ:
  -- ALTER DATABASE Sample RENAME TO Example

-- ЗАВДАННЯ 3
-- Видаліть базу даних Example.
--РІШЕННЯ:
  -- DROP DATABASE Example

-- ЗАВДАННЯ 4
-- Створіть базу даних для зберігання оцінок студентів.
--РІШЕННЯ:
--	CREATE DATABASE STUDENT_GRADES;

-- У базі даних створіть таблицю «Оцінки студентів», яка зберігатиме таку інформацію:
-- ■ ПІБ студента;
-- ■ місто;
-- ■ країна;
-- ■ дата народження;
-- ■ електронна адреса;
-- ■ контактний телефон;
-- ■ назва групи;
-- ■ середня оцінка за рік з усіх предметів;
-- ■ назва предмета з мінімальною, середньою оцінкою;
-- ■ назва предмета з максимальною, середньою оцінкою.
--РІШЕННЯ:
	-- CREATE TABLE STUDENTS(
	-- 	ID SERIAL,
	-- 	NAME VARCHAR(50),
	-- 	CITY VARCHAR(20),
	-- 	COUNTRY VARCHAR(20),
	-- 	BIRTHDAY INT,
	-- 	EMAIL VARCHAR(50),
	-- 	PHONE VARCHAR(13),
	-- 	GROUP_NAME VARCHAR(20),
	-- 	AVG_GRADE_YEAR INT,
	-- 	MIN_GRADE INT,
	-- 	MAX_GRADE INT,
	-- 	NAME_SUBJECT_MIN VARCHAR(20),
	-- 	NAME_SUBJECT_MAX VARCHAR(20)
	-- 	)

-- Наповніть цю базу даних трьома студентами.
-- РІШЕННЯ:
-- 	INSERT INTO STUDENTS (
-- 		NAME,
-- 	    CITY,
-- 	    COUNTRY,
-- 	    BIRTHDAY,
-- 	    EMAIL,
-- 	    PHONE,
-- 	    GROUP_NAME,
-- 	    AVG_GRADE_YEAR,
-- 	    MIN_GRADE,
-- 	    MAX_GRADE,
-- 	    NAME_SUBJECT_MIN,
-- 	    NAME_SUBJECT_MAX
-- 		)
-- VALUES
-- ('John Smith', 'New York', 'USA', 2001, 'john.smith@gmail.com', '+12025550101', 'Python-21', 84, 60, 98, 'Physics', 'Math'),
-- ('Emma Johnson', 'London', 'UK', 2000, 'emma.johnson@gmail.com', '+447700900101', 'Python-21', 91, 72, 100, 'History', 'English'),
-- ('Liam Brown', 'Toronto', 'Canada', 2002, 'liam.brown@gmail.com', '+14165550102', 'Data-11', 77, 55, 90, 'Math', 'Biology'),
-- ('Olivia Davis', 'Sydney', 'Australia', 2001, 'olivia.davis@gmail.com', '+6125550103', 'Data-11', 88, 70, 99, 'Physics', 'Chemistry'),
-- ('Noah Wilson', 'Berlin', 'Germany', 1999, 'noah.wilson@gmail.com', '+491511000104', 'AI-31', 80, 61, 95, 'English', 'Programming'),

-- ('Sophia Miller', 'Paris', 'France', 2003, 'sophia.miller@gmail.com', '+3315550105', 'AI-31', 93, 75, 100, 'Math', 'Programming'),
-- ('James Taylor', 'Madrid', 'Spain', 2000, 'james.taylor@gmail.com', '+34915550106', 'Web-15', 69, 50, 82, 'Physics', 'History'),
-- ('Isabella Anderson', 'Rome', 'Italy', 2002, 'isabella.anderson@gmail.com', '+39065550107', 'Web-15', 85, 64, 97, 'Chemistry', 'English'),
-- ('Benjamin Thomas', 'Kyiv', 'Ukraine', 2001, 'benjamin.thomas@gmail.com', '+380671110108', 'SQL-07', 79, 58, 91, 'Biology', 'Math'),
-- ('Mia Jackson', 'Warsaw', 'Poland', 2000, 'mia.jackson@gmail.com', '+48501110109', 'SQL-07', 90, 73, 100, 'History', 'Programming'),

-- ('Lucas White', 'Prague', 'Czechia', 2003, 'lucas.white@gmail.com', '+420601110110', 'Python-21', 74, 52, 88, 'English', 'Physics'),
-- ('Charlotte Harris', 'Vienna', 'Austria', 2002, 'charlotte.harris@gmail.com', '+43111110111', 'Python-21', 95, 80, 100, 'History', 'Programming'),
-- ('Henry Martin', 'Amsterdam', 'Netherlands', 1999, 'henry.martin@gmail.com', '+31201110112', 'Data-11', 81, 60, 94, 'Math', 'English'),
-- ('Amelia Thompson', 'Brussels', 'Belgium', 2001, 'amelia.thompson@gmail.com', '+32211110113', 'Data-11', 87, 66, 98, 'Physics', 'Biology'),
-- ('Alexander Garcia', 'Lisbon', 'Portugal', 2000, 'alex.garcia@gmail.com', '+35191110114', 'AI-31', 92, 71, 100, 'Chemistry', 'Programming'),

-- ('Evelyn Martinez', 'Dublin', 'Ireland', 2002, 'evelyn.martinez@gmail.com', '+353851110115', 'AI-31', 83, 63, 96, 'History', 'Math'),
-- ('Daniel Robinson', 'Oslo', 'Norway', 2001, 'daniel.robinson@gmail.com', '+47911110116', 'Web-15', 76, 57, 89, 'Biology', 'Programming'),
-- ('Harper Clark', 'Stockholm', 'Sweden', 2003, 'harper.clark@gmail.com', '+4681110117', 'Web-15', 89, 69, 99, 'Physics', 'English'),
-- ('Matthew Lewis', 'Helsinki', 'Finland', 1998, 'matthew.lewis@gmail.com', '+358401110118', 'SQL-07', 71, 50, 85, 'Math', 'Chemistry'),
-- ('Abigail Walker', 'Copenhagen', 'Denmark', 2000, 'abigail.walker@gmail.com', '+45321110119', 'SQL-07', 94, 78, 100, 'History', 'Programming'),

-- ('David Hall', 'Zurich', 'Switzerland', 2001, 'david.hall@gmail.com', '+41441110120', 'Python-21', 82, 62, 93, 'English', 'Math'),
-- ('Emily Allen', 'Budapest', 'Hungary', 2002, 'emily.allen@gmail.com', '+3611110121', 'Python-21', 88, 67, 98, 'Biology', 'Programming'),
-- ('Joseph Young', 'Athens', 'Greece', 1999, 'joseph.young@gmail.com', '+30211110122', 'Data-11', 73, 54, 87, 'Physics', 'English'),
-- ('Ella King', 'Sofia', 'Bulgaria', 2003, 'ella.king@gmail.com', '+359881110123', 'Data-11', 91, 74, 100, 'Math', 'Programming'),
-- ('Samuel Wright', 'Bucharest', 'Romania', 2000, 'samuel.wright@gmail.com', '+40111110124', 'AI-31', 78, 59, 90, 'Chemistry', 'Biology'),

-- ('Grace Scott', 'Belgrade', 'Serbia', 2001, 'grace.scott@gmail.com', '+381611110125', 'AI-31', 96, 82, 100, 'History', 'Programming'),
-- ('Michael Green', 'Kyiv', 'Ukraine', 2002, 'michael.green@gmail.com', '+380501110126', 'Web-15', 84, 65, 95, 'Physics', 'Math'),
-- ('Chloe Baker', 'Lviv', 'Ukraine', 2000, 'chloe.baker@gmail.com', '+380671110127', 'Web-15', 86, 68, 97, 'English', 'Programming'),
-- ('Ethan Adams', 'Kharkiv', 'Ukraine', 1999, 'ethan.adams@gmail.com', '+380931110128', 'SQL-07', 75, 56, 88, 'Biology', 'Chemistry'),
-- ('Avery Nelson', 'Odesa', 'Ukraine', 2003, 'avery.nelson@gmail.com', '+380991110129', 'SQL-07', 93, 77, 100, 'History', 'Programming');

	-- SELECT *
	-- FROM STUDENTS


-- ЗАВДАННЯ 5
-- Створіть наступні запити для таблиці з оцінками
-- студентів із попереднього завдання:
-- ■ Відображати всієї інформації з таблиці зі студентами та оцінками.
--РІШЕННЯ:
	-- SELECT *
	-- FROM STUDENTS

-- ■ Відображати ПІБ усіх студентів.
--РІШЕННЯ:
	-- SELECT NAME
	-- FROM STUDENTS

-- ■ Відображати усіх середніх оцінок.
--РІШЕННЯ:
	-- SELECT AVG_GRADE_YEAR
	-- FROM STUDENTS

-- ■ Показати ПІБ усіх студентів з мінімальною оцінкою, більшою, ніж зазначена.
--РІШЕННЯ:
	-- SELECT NAME
	-- FROM STUDENTS
	-- WHERE MIN_GRADE > 70

-- ■ Показати країни студентів. Назви країн мають бути унікальними.
--РІШЕННЯ:
	-- SELECT DISTINCT COUNTRY
	-- FROM STUDENTS

-- ■ Показати міста студентів. Назви міст мають бути унікальними.
--РІШЕННЯ:
	-- SELECT DISTINCT CITY
	-- FROM STUDENTS

-- ■ Показати назви груп. Назви груп мають бути унікальними.
--РІШЕННЯ:
	-- SELECT DISTINCT GROUP_NAME
	-- FROM STUDENTS

-- ■ Показати назви усіх предметів із мінімальними середніми оцінками. Назви предметів мають бути унікальними.
--РІШЕННЯ:
	-- SELECT DISTINCT NAME_SUBJECT_MIN, MIN_GRADE
	-- FROM STUDENTS
