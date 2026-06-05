-- Курс: «Введення в мову
-- програмування Python
-- Модуль 15. Вступ до теорії баз даних
-- Тема: Вступ до теорії баз даних. Частина 1
-- Завдання 1
-- Створіть базу даних під назвою Birds. Розташування залишається на ваш вибір.
--РІШЕННЯ:
	CREATE DATABASE BIRDS

-- Завдання 2
-- Переназвіть базу даних із першого завдання. Нове ім’я для бази даних Cats.
--РІШЕННЯ:
	ALTER DATABASE BIRDS RENAME TO CATS

-- Завдання 3
-- Видаліть базу даних Cats.
--РІШЕННЯ:
	DROP DATABASE CATS
	DROP TABLE VEG_FRUIT

-- Завдання 4
-- Створіть однотабличну базу даних «Овочі та фрукти», яка зберігатиме таку інформацію:
-- ■ Назва;
-- ■ Тип (овоч або фрукт);
-- ■ Колір;
-- ■ Калорійність;
-- ■ Короткий опис.
--РІШЕННЯ:
	CREATE TABLE VEG_FRUIT (
	 	ID SERIAL,
	 	NAME VARCHAR(15),
	 	TYPE VARCHAR(10),
	 	COLOR VARCHAR(10),
	 	CALORY INT,
	 	DESCRIPTION VARCHAR(100)
	    )
	 INSERT INTO VEG_FRUIT (
	 	NAME,
	 	TYPE,
	 	COLOR,
	 	CALORY,
	 	DESCRIPTION
	 )

	 VALUES
	 ('Apple', 'Fruit', 'Red', 52, 'Sweet and juicy fruit'),
	 ('Banana', 'Fruit', 'Yellow', 89, 'Soft tropical fruit'),
	 ('Orange', 'Fruit', 'Orange', 47, 'Citrus fruit'),
	 ('Pear', 'Fruit', 'Green', 57, 'Sweet green fruit'),
	 ('Grape', 'Fruit', 'Purple', 69, 'Small juicy berries'),
	 ('Peach', 'Fruit', 'Orange', 39, 'Soft summer fruit'),
	 ('Cherry', 'Fruit', 'Red', 50, 'Small sweet fruit'),
	 ('Lemon', 'Fruit', 'Yellow', 29, 'Sour citrus fruit'),
	 ('Kiwi', 'Fruit', 'Brown', 61, 'Fruit with green inside'),
	 ('Mango', 'Fruit', 'Orange', 60, 'Tropical sweet fruit'),

	 ('Tomato', 'Vegetable', 'Red', 18, 'Popular salad vegetable'),
	 ('Cucumber', 'Vegetable', 'Green', 15, 'Fresh crunchy vegetable'),
	 ('Potato', 'Vegetable', 'Brown', 77, 'Common root vegetable'),
	 ('Carrot', 'Vegetable', 'Orange', 41, 'Vegetable rich in vitamins'),
	 ('Onion', 'Vegetable', 'White', 40, 'Vegetable with strong smell'),
	 ('Pepper', 'Vegetable', 'Red', 20, 'Sweet bell pepper'),
	 ('Eggplant', 'Vegetable', 'Purple', 25, 'Soft textured vegetable'),
	 ('Cabbage', 'Vegetable', 'Green', 25, 'Leafy green vegetable'),
	 ('Broccoli', 'Vegetable', 'Green', 34, 'Healthy green vegetable'),
	 ('Corn', 'Vegetable', 'Yellow', 86, 'Sweet yellow vegetable');

-- Завдання 5
-- Створіть наступні запити для таблиці з інформацією про овочі та фрукти із попереднього завдання:

-- ■ Відображення всієї інформації з таблиці овочів та фруктів;
--РІШЕННЯ:
	 SELECT *
	 FROM VEG_FRUIT

-- ■ Відображення усіх овочів;
--РІШЕННЯ:
	 SELECT *
	 FROM VEG_FRUIT
	 WHERE TYPE = 'Vegetable';

-- ■ Відображення усіх фруктів;
--РІШЕННЯ:
	 SELECT *
	 FROM VEG_FRUIT
	 WHERE TYPE = 'Fruit';

-- ■ Відображення усіх назв овочів та фруктів;
--РІШЕННЯ:
	 SELECT NAME
	 FROM VEG_FRUIT

-- ■ Відображення усіх кольорів. Кольори мають бути унікальними;
--РІШЕННЯ:
	 SELECT DISTINCT COLOR
	 FROM VEG_FRUIT

-- ■ Відображення фруктів певного кольору;
--РІШЕННЯ:
	 SELECT NAME, TYPE, COLOR
	 FROM VEG_FRUIT
	 WHERE TYPE = 'Fruit' AND COLOR = 'Orange'

-- ■ Відображення овочів певного кольору.
--РІШЕННЯ:
	 SELECT NAME, TYPE, COLOR
	 FROM VEG_FRUIT
	 WHERE TYPE = 'Vegetable' AND COLOR IN ('Green', 'Yellow')
