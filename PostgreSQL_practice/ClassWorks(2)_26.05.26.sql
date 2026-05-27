 Завдання 1
 Створіть наступні запити для бази даних з оцінками студентів із попереднього практичного завдання:
	 SELECT *
	 FROM STUDENTS

 ■ Показати ПІБ усіх студентів з мінімальною оцінкою у вказаному діапазоні.
	 SELECT NAME, MIN_GRADE
	 FROM STUDENTS
	 WHERE MIN_GRADE < 80 AND MIN_GRADE > 70

 Змінити тип даних у стовпчику "BIRTHDAY"
	 ALTER TABLE STUDENTS
	 DROP COLUMN BIRTHDAY

 Створити стовпчик "BIRTHDAY" з новим типом даних
	 ALTER TABLE STUDENTS
	 ADD COLUMN BIRTHDAY DATE

	 UPDATE STUDENTS
	 SET BIRTHDAY = '2000-01-01'

 ■ Показати інформацію про студентів, яким виповнилося 20 років.
	 SELECT NAME, AGE(BIRTHDAY)
	 FROM STUDENTS
	 WHERE  AGE(BIRTHDAY) > INTERVAL '20 years'

 ■ Показати інформацію про студентів з віком, у вказаному діапазоні.
	 SELECT NAME, AGE(BIRTHDAY)
	 FROM STUDENTS
	 WHERE AGE(BIRTHDAY)
	 BETWEEN INTERVAL '20 years'
	 AND INTERVAL '27 years'

 ■ Показати інформацію про студентів із конкретним ім’ям. Наприклад, показати студентів з ім’ям Борис.
	 SELECT NAME
	 FROM STUDENTS
	 WHERE NAME ILIKE 'SOPHIA%'

 ■ Показати інформацію про студентів, в номері яких є три сімки.
	 SELECT NAME, PHONE
	 FROM STUDENTS
	 WHERE PHONE ILIKE '%1%1%1%'

 ■ Показати електронні адреси студентів, що починаються з конкретної літери.
	 SELECT NAME, EMAIL
	 FROM STUDENTS
	 WHERE EMAIL LIKE 'd%'


 ЗАВДАННЯ 2
 Створіть наступні запити для бази даних з оцінками студентів із попереднього практичного завдання:
 ■ Показати мінімальну середню оцінку по всіх студентах.
	 SELECT NAME, MIN_GRADE
	 FROM STUDENTS


 ■ Показати максимальну середню оцінку по всіх студентах.
	 SELECT NAME, MAX_GRADE
	 FROM STUDENTS

 ■ Показати статистику міст. Має відображатися назва міста та кількість студентів з цього міста.
	 SELECT CITY, COUNT(*)
	 FROM STUDENTS
	 GROUP BY CITY

 ■ Показати статистику студентів. Має відображатися назва країни та кількість студентів з цієї країни.
	 SELECT COUNTRY, COUNT(*)
	 FROM STUDENTS
	 GROUP BY COUNTRY

 ■ Показати кількість студентів з мінімальною середньою оцінкою з математики.
	 SELECT NAME, COUNT(*)
	 FROM STUDENTS
	 WHERE NAME_SUBJECT_MIN = 'Math'
	 GROUP BY NAME

 ■ Показати кількість студентів з максимальною середньою оцінкою з математики.
	 SELECT NAME, COUNT(*), MAX_GRADE
	 FROM STUDENTS
	 WHERE NAME_SUBJECT_MAX = 'Math'
	 GROUP BY NAME, MAX_GRADE

 ■ Показати кількість студентів у кожній групі.
	 SELECT GROUP_NAME, COUNT(*) AS COUNT_STUDENTS
	 FROM STUDENTS
	 GROUP BY GROUP_NAME

 ■ Показати середню оцінку групи.
	 SELECT GROUP_NAME, AVG_GRADE_YEAR
	 FROM STUDENTS

--- ДОДАТКОВІ ЗАВДАННЯ -----

 ВИВЕСТИ МАКСИМАЛЬНУ СЕРЕДНЮ ОЦІНКУ
	 SELECT MAX(AVG_GRADE_YEAR)
	 FROM STUDENTS

 ВИВЕСТИ ВМ'Я СТУДЕНТА, ЯКИЙ ОТРИМАВ МАКСИМАЛЬНУ СЕРЕДНЮ ОЦІНКУ
	 SELECT *
	 FROM STUDENTS
	 WHERE AVG_GRADE_YEAR = (
	 		SELECT MAX(AVG_GRADE_YEAR)
	 		FROM STUDENTS
	 )

 ВИВЕСТИ СТУДЕНТІВ ЯКІ НАВЧАЮТЬСЯ В ГРУПІ З НАЙВИЩОЮ СЕРЕДНЬОЇ ОЦІНКОЮ
	 SELECT NAME, MAX_GRADE
	 FROM STUDENTS


 ВИВЕСТИ МІСТА І КІЛЬКІСТЬ СТУДЕНТІВ
	 SELECT CITY, COUNT(*)
	 FROM STUDENTS
	 GROUP BY CITY

 ВИВЕСТИ НАЙБІЛЬШУ КІЛЬКІСТЬ СТУДЕНТІВ СЕРЕД МІСТ
	 WITH STUDENT_CITY AS (
	 	SELECT CITY, COUNT(*)
	 	FROM STUDENTS
	 	GROUP BY CITY
	 )
	 SELECT MAX(COUNT)
	 FROM STUDENT_CITY


 ВИВЕСТИ ГРУПИ І ЇХНІ СЕРЕДНІ ОЦІНКИ
	 WITH GROUP_INFO AS (
	 	SELECT GROUP_NAME, 	ROUND (AVG(AVG_GRADE_YEAR), 2) AS GROUP_GRADE
	 	FROM STUDENTS
	 	GROUP BY GROUP_NAME
	 )
	 SELECT GROUP_NAME, GROUP_GRADE
	 FROM GROUP_INFO
	 WHERE GROUP_GRADE = (
	 	SELECT MAX(GROUP_GRADE)
	 	FROM GROUP_INFO
	 	)
