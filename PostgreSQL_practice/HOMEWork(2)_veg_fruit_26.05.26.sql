-- Курс: «Введення в мову
-- програмування Python
-- Модуль 15. Вступ до теорії баз даних
-- Тема: Вступ до теорії баз даних.
-- Частина 2

-- Завдання 1
-- Створіть наступні запити для бази даних з інформацією
-- про овочі та фрукти з попереднього домашнього завдання:
	-- SELECT *
	-- FROM VEG_FRUIT

-- ■ Відображення усіх овочів з калорійністю, менше вказаної.
	-- SELECT *
	-- FROM VEG_FRUIT
	-- WHERE CALORY <= '50'

-- ■ Відображення усіх фруктів з калорійністю у вказаному діапазоні.
	-- SELECT *
	-- FROM VEG_FRUIT
	-- WHERE CALORY BETWEEN '30' AND '80'

-- ■ Відображення усіх овочів, у назві яких є вказане слово.
-- Наприклад, слово: капуста.
	-- SELECT *
	-- FROM VEG_FRUIT
	-- WHERE NAME = 'Cabbage'

-- ■ Відображення усіх овочів та фруктів, у короткому описі яких є вказане слово.
-- Наприклад, слово: гемоглобін.
	-- SELECT *
	-- FROM VEG_FRUIT
	-- WHERE DESCRIPTION LIKE '%hemoglobin%'
	-- 	OR DESCRIPTION LIKE '%green%'

-- ■ Показати усі овочі та фрукти жовтого або червоного кольору.
	-- SELECT *
	-- FROM VEG_FRUIT
	-- WHERE COLOR = 'Yellow'
	-- 	OR COLOR = 'Red'

-- Завдання 2
-- Створіть наступні запити для бази даних з інформацією
-- про овочі та фрукти з попереднього домашнього завдання:
-- ■ Показати кількість овочів.
	-- SELECT COUNT(*) AS VEGETABLE_COUNT
	-- FROM VEG_FRUIT
	-- WHERE TYPE = 'Vegetable'

-- ■ Показати кількість фруктів.
	-- SELECT COUNT(*) AS FRUIT_COUNT
	-- FROM VEG_FRUIT
	-- WHERE TYPE = 'Fruit'

-- ■ Показати кількість овочів та фруктів заданого кольору.
	-- SELECT COUNT(*) AS VEG_FRUIT_COUNT
	-- FROM VEG_FRUIT
	-- WHERE COLOR = 'Yellow'

-- ■ Показати кількість овочів та фруктів кожного кольору.
	-- SELECT COLOR, COUNT(*) AS COUNT_PROD
	-- FROM VEG_FRUIT
	-- GROUP BY COLOR

-- ■ Показати колір мінімальної кількості овочів та фруктів.
	-- WITH COUNT_COLOR AS (
	-- 	SELECT COLOR, COUNT(*) AS COUNT_PRODUCT
	-- 	FROM VEG_FRUIT
	-- 	GROUP BY COLOR
	-- )
	-- SELECT *
	-- FROM COUNT_COLOR
	-- WHERE COUNT_PRODUCT = (
	-- 	SELECT MIN(COUNT_PRODUCT)
	-- 	FROM COUNT_COLOR
	-- )

-- ■ Показати колір максимальної кількості овочів та фруктів.
	-- WITH COUNT_COLOR AS (
	-- 	SELECT COLOR , COUNT(*) AS COUNT_PROD
	-- 	FROM VEG_FRUIT
	-- 	GROUP BY COLOR
	-- )
	-- SELECT *
	-- FROM COUNT_COLOR
	-- WHERE COUNT_PROD = (
	-- 	SELECT MAX(COUNT_PROD)
	-- 	FROM COUNT_COLOR
	-- )

-- ■ Показати мінімальну калорійність овочів та фруктів.
	-- SELECT *
	-- FROM VEG_FRUIT
	-- WHERE CALORY = (
	-- 	SELECT MIN(CALORY)
	-- 	FROM VEG_FRUIT
	-- )

-- ■ Показати максимальну калорійність овочів та фруктів.
	-- SELECT *
	-- FROM VEG_FRUIT
	-- WHERE CALORY = (
	-- 	SELECT MAX(CALORY)
	-- 	FROM VEG_FRUIT
	-- )

-- ■ Показати середню калорійність овочів та фруктів.
	-- SELECT ROUND(AVG(CALORY),2) AS AVG_CALORY_PROD
	-- FROM VEG_FRUIT

-- ■ Показати фрукт з мінімальною калорійністю
	-- SELECT NAME, CALORY
	-- FROM VEG_FRUIT
	-- WHERE CALORY = (
	-- 	SELECT MIN(CALORY)
	-- 	FROM VEG_FRUIT
	-- )

-- ■ Показати фрукт з максимальною калорійністю (через WITH)
	-- WITH MAX_FRUIT_CALORY AS (
	-- 	SELECT MAX(CALORY) AS MAX_CALORY
	-- 	FROM VEG_FRUIT
	-- 	WHERE TYPE = 'Fruit'
	-- )
	-- SELECT NAME, CALORY
	-- FROM VEG_FRUIT
	-- WHERE TYPE = 'Fruit'
	-- 		AND CALORY = (
	-- 			SELECT MAX_CALORY
	-- 			FROM MAX_FRUIT_CALORY
			)
