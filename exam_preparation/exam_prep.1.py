# Підготовка до екзамену
# Курс «AI + Python»
# Частин: 2 Тем: 12 Завдань: 100+
import random
from calendar import month
from wsgiref.validate import check_input

# ЧАСТИНА 1 ОСНОВИ - Python -
# ВИВІД, ВИВІД та АРИФМЕТИЧНІ ОПЕРАЦІЇ

# 1. Добуток двох чисел
# Введіть два числа з клавіатури та виведіть результат їхнього множення.
# Підказка: Використайте input() та перетворення на int або float.
print("ДОБУТОК 2-х ЧИСЕЛ")

num1 = float(input("Введіть 1-ше число: "))
num2 = float(input("Введіть 2-uе число: "))

result = num1 * num2
print("Добуток чисел:", result)

# 2. Середнє арифметичне
# Введіть три числа. Обчисліть та виведіть їх середнє арифметичне.
# Підказка: Середнє = сума / кількість чисел.
print("\nСЕРЕДНЄ АРИФМЕТИЧНЕ ЧИСЛО")

num1 = float(input("\nВведіть 1-ше число: "))
num2 = float(input("Введіть 2-ге число: "))
num3 = float(input("Введіть 3-тє число: "))

average = (num1 + num2 + num3) / 3
print("Середнє арифметичне: ", round(average, 2))

# 3. Площа прямокутника
# Введіть довжину та ширину прямокутника. Виведіть його площу.
# Підказка: Площа = довжина * ширина.
print("\nПЛОЩА ПРЯМОКУТНИКА")

rectangle_length = float(input("\nВведіть довжину прямокутника: "))
rectangle_width = float(input("Введіть ширину прямокутника: "))

rectangle_area = rectangle_length * rectangle_width
print("Площа прямокутника: ", rectangle_area)

# 4. Периметр трикутника
# Введіть три сторони трикутника. Обчисліть та виведіть периметр.
# Підказка: Периметр = a + b + c.
print("\nПЕРИМЕТР ТРИКУТНИКА")

triangle_side1 = float(input("\nВведіть 1-шу сторону трикутника: "))
triangle_side2 = float(input("\nВведіть 2-гу сторону трикутника: "))
triangle_side3 = float(input("\nВведіть 3-тю сторону трикутника: "))

triangle_area = triangle_side1 + triangle_side2 + triangle_side3
print("Периметр трикутника: ", triangle_area)

# 5. Конвертація температури
# Введіть температуру в градусах Цельсія. Перетворіть і виведіть значення у Фаренгейтах.
# Підказка: Формула: F = C * 9/5 + 32.
print("\nКОНВЕРТАЦІЯ ТЕМПЕРАТУРИ")

temperature = float(input("\nВведіть температуру (Цельсій): "))

fahrenheit = temperature * 9 / 5 + 32
print("Температура у Фаренгейт: ", fahrenheit)

# 6. Конвертація часу
# Введіть кількість хвилин. Виведіть відповідь у форматі "X год Y хв".
# Підказка: Використайте оператори // та %.
print("\nКОНВЕРТАЦІЯ ЧАСУ")

minutes = float(input("\nВведіть кількість хвилин: "))

hours = minutes // 60
minutes = minutes % 60

print("Кількість годин: ", hours, "кількість хвилин: ", minutes)

# 7. Остача від ділення
# Введіть два числа. Виведіть остачу від ділення першого на друге.
# Підказка: Оператор % повертає остачу.
print("\nОСТАЧА ВІД ДІЛЕННЯ")

num_1 = float(input("\nВведіть 1-ше число: "))
num_2 = float(input("\nВведіть 2-ге число: "))

remainder = num_1 % num_2

print("Залишок від ділення першого на друге: ", remainder)

# 8. Перевірка парності
# Введіть ціле число. Визначте та виведіть, чи є воно парним чи непарним.
# Підказка: Число парне, якщо n % 2 == 0.
print("\nПЕРЕВІРКА ПАРНОСТІ")

integer = float(input("Введіть ціле число: "))

if integer % 2 == 0:
    print("Число -", integer, "є парне")
else:
    print("Число - ", integer, "є НЕ парне")

# 9. Ділення на 3 і 5
# Введіть ціле число. Визначте, чи ділиться воно одночасно на 3 і на 5. Виведіть
# відповідь.
# Підказка: Умова: n % 3 == 0 and n % 5 == 0.
print("\nДІЛЕННЯ НА 3 і 5")

integer_num = float(input("Введіть ціле число: "))

if integer_num % 2 == 0 and integer_num % 5 == 0:
    print("ТАК, число", integer_num, "ділиться на 3 і 5")
else:
    print("НІ, число", integer_num, "НЕ ділиться на 3 і 5")

# 10. Вартість зі знижкою
# Введіть початкову ціну товару та відсоток знижки. Обчисліть і виведіть кінцеву вартість.
# Підказка: Кінцева ціна = ціна * (1 - знижка / 100).
print("\nВАРТІСТЬ ЗІ ЗНИЖКОЮ")

price = float(input("Введіть ціну товару: "))
discount = float(input("Введіть відсоток знижки (числом): "))

cost_product = price * (1 - discount / 100)

#   --- УМОВНІ ОПЕРАТОРИ ---

# 11. Більше з двох чисел
# Введіть два числа. Визначте і виведіть, яке з них більше, або повідомте, що вони рівні.
# Підказка: Використайте if / elif / else.
print("\nБІЛЬШЕ З ДВОХ ЧИСЕЛ")

num1 = float(input("Введіть 1-ше число: "))
num2 = float(input("Введіть 2-uе число: "))

if num1 > num2:
    print(f"Число {num1} більше")
elif num1 < num2:
    print(f"Число {num2} більше")
else:
    print("Введені числа рівні")

# 12. Найбільше з трьох чисел
# Введіть три числа. Знайдіть і виведіть найбільше з них без використання функції max().
# Підказка: Порівнюйте попарно: якщо a > b і a > c, то a — найбільше.
print("\nНАЙБІЛЬШЕ З ТРЬОХ ЧИСЕЛ")

num1 = float(input("Введіть 1-ше число: "))
num2 = float(input("Введіть 2-uе число: "))
num3 = float(input("Введіть 3-тє число: "))

if num1 >= num2 and num1 >= num3:
    print(f"Найбільше число - {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"Найбільше число - {num2}")
else:
    print(f"Найбільше число {num3}")

# 13. Знак числа
# Введіть число. Визначте та виведіть: додатне воно, від'ємне, чи нуль.
# Підказка: Три гілки: n > 0, n < 0, n == 0.
print("\nЗНАК ЧИСЛА")

number = float(input("Введіть число: "))

if number > 0:
    print(number, "Додатне число")
elif number < 0:
    print(number, "Від'ємне число")
elif number == 0:
    print(number, "НУЛЬ")

# 14. Оцінка за балом
# Введіть бал від 0 до 100. Виведіть оцінку: 90–100 → 12 балів, 75–89 → 9–11, 60–74 → 6–8, нижче 60 → незадовільно.
# Підказка: Використайте elif для кожного діапазону.
print("\nОЦІНКА ЗА БАЛОМ")

points = int(input("Введіть бал від '0' до '100': "))

if 90 <= points <= 100:
    print("Ваша оцінка '12' балів")
elif 75 <= points <= 89:
    print("Ваша оцінка '9-11' балів")
elif 60 <= points <= 74:
    print("Ваша оцінка '6-8' балів")
else:
    print("Ваша оцінка 'НЕЗАДОВІЛЬНО'")

# 15. Високосний рік
# Введіть рік. Визначте, чи є він високосним, і виведіть відповідь.
# Підказка: Рік високосний, якщо ділиться на 4, але не на 100, або ділиться на 400.
print("ВИСОКОСНИЙ РІК")

year = int(input("Введіть рік: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Введений рік є ВИСОКОСНИМ!")
else:
    print("Введений рік НЕ є високосним!")

# 16. Існування трикутника
# Введіть три сторони. Перевірте, чи може існувати трикутник з такими сторонами.
# Підказка: Трикутник існує, якщо сума будь-яких двох сторін більша за третю.
print("\nІСНУВАННЯ ТРИКУТНИКА")

triangle_side1 = float(input("\nВведіть 1-шу сторону: "))
triangle_side2 = float(input("\nВведіть 2-гу сторону: "))
triangle_side3 = float(input("\nВведіть 3-тю сторону: "))

if triangle_side1 + triangle_side2 > triangle_side3 or triangle_side2 + triangle_side3 > triangle_side1:
    print("Вказані сторони сформують ТРИКУТНИК")
else:
    print("Вказані сторони не сформують трикутник")

# 17. Тип трикутника
# Введіть три сторони. Визначте тип трикутника: рівносторонній, рівнобедрений або різносторонній.
# Підказка: Рівносторонній: a==b==c; рівнобедрений: дві сторони рівні; решта — різносторонній.
print("\nТИП ТРИКУТНИКА")

triangle_a = float(input("\nВведіть 1-шу сторону трикутника: "))
triangle_b = float(input("\nВведіть 2-гу сторону трикутника: "))
triangle_c = float(input("\nВведіть 3-тю сторону трикутника: "))

# Перевірка існування трикутника
if (
        triangle_a + triangle_b > triangle_c
        and triangle_a + triangle_c > triangle_b
        and triangle_b + triangle_c > triangle_a
):
    print("Трикутник існує")

if triangle_a == triangle_b == triangle_c:
    print("Трикутник РІВНОСТОРОННІЙ")
elif triangle_a == triangle_b or triangle_a == triangle_c or triangle_b == triangle_c:
    print("Трикутник РІВНОБЕДРЕНИЙ")
else:
    print("Трикутник РІЗНОСТОРОННІЙ")

# 18. Перевірка пароля
# Задайте правильний пароль у коді. Введіть пароль з клавіатури та виведіть, чи він правильний.
# Підказка: Порівняйте введений рядок з еталонним через ==.
print("\nПЕРЕВІРКА ПАРОЛЯ")

password = "IT_Step_2026"
input_pass = input("Введіть пароль: ")

if input_pass == password:
    print("Пароль вірний!")
else:
    print("Ви ввели НЕ вірний пароль")

# 19. Система входу
# Задайте логін і пароль у коді. Введіть їх з клавіатури. Виведіть "Вхід успішний" або "Помилка".
# Підказка: Перевіряйте обидві умови одночасно через and.
print("\nСИСТЕМА ВХОДУ")

login = "GOstepIT@gmail.com"
password = "IT_Step_2026"

input_login = input("Введіть логін: ")
input_password = input("Введіть пароль: ")

if input_login == login and input_password == password:
    print("Вхід успішний!")
else:
    print("ПОМИЛКА. Ви ввели не вірний логін або пароль")

# 20. Пора року
# Введіть номер місяця (1–12). Виведіть відповідну пору року.
# Підказка: Зима: 12,1,2; Весна: 3,4,5; Літо: 6,7,8; Осінь: 9,10,11. Використайте оператор in.
print("\nПОРА РОКУ!")

month = int(input("Введіть номер місяця (від 1 до 12:"))

if month in (1, 2, 12):
    print("Пора року 'ЗИМА' ")
elif month in (3, 4, 5):
    print("пора року 'ВЕСНА' ")
elif month in (6, 7, 8):
    print("Пора року 'ЛІТО' ")
elif month in (9, 10, 11):
    print("Пора року 'ОСІНЬ' ")
else:
    print("Введено не коректне число")

#   --- ЦИКЛ WHILE ---

# 21. Числа від 1 до 20
# Використовуючи цикл while, виведіть усі числа від 1 до 20 через пробіл або кожне на новому рядку.
# Підказка: Ініціалізуйте лічильник i = 1, збільшуйте на 1 поки i <= 20.
print("\n ЧИСЛА ВІД 1 до 20")
i = 1

while i <= 20:
    print("Число", i)
    i += 1

# 22. Числа від 20 до 1
# Використовуючи цикл while, виведіть усі числа від 20 до 1 у зворотному порядку.
# Підказка: Ініціалізуйте i = 20, зменшуйте на 1 поки i >= 1.
print("\n ЧИСЛА ВІД 20 до 1")
i = 20

while i >= 20:
    print("Число", i)
    i -= 1

# 23. Сума від 1 до N
# Введіть число N. За допомогою while обчисліть і виведіть суму всіх чисел від 1 до N.
# Підказка: Накопичуйте суму: total += i на кожному кроці.
print("\n СУМА ВІД 1 до N")
n = int(input("Введіть число від 1 до n: "))

i = 1
total = 0

while i <= n:
    total += i
    i += 1

print("Сума всіх чисел =", total)

# 24. Добуток від 1 до N
# Введіть число N. За допомогою while обчисліть добуток усіх чисел від 1 до N (факторіал).
# Підказка: Ініціалізуйте result = 1, множте на i на кожному кроці.
print("\n ДОБУТОК ВІД 1 до N")
n = int(input("Введіть ЦІЛЕ число: "))

i = 1
result = 1

while i <= n:
    result *= i
    i += 1

print(f"добуток чисел від 1 до {n} =", total)

# 25. Факторіал числа
# Введіть ціле невід'ємне число N. Обчисліть і виведіть його факторіал (N!).
# Підказка: Факторіал 0 і 1 дорівнює 1. Далі: n! = 1 * 2 * 3 * ... * n.
print("\nФАКТОРІАЛ ЧИСЛА")
n = int(input("Введіть ЦІЛЕ невід'ємне число: "))

factorial = 1
i = 1

while i <= n:
    factorial *= i
    i += 1

print(f"Факторіал числа {n} =", factorial)

# 26. Введення до нуля
# Постійно просіть користувача вводити числа, поки він не введе 0. Тоді завершіть програму.
# Підказка: Умова циклу: while True, вихід — break або while число != 0.
print("\nВВЕДЕННЯ ДО НУЛЯ")

while True:
    n = int(input("Введіть ЦІЛЕ невід'ємне число: "))
    if n == 0:
        print("Програму завершено")
        break

# 27. Кількість введень
# Просіть вводити числа до введення 0. Порахуйте і виведіть кількість введених чисел (без нуля).
# Підказка: Використайте лічильник count, збільшуйте після кожного введення.
print("\nКІЛЬКІСТЬ ВВЕДЕНЬ")

count = 1
while True:
    n = int(input("Введіть ЦІЛЕ невід'ємне число: "))
    if n == 0:
        print("Програму завершено!\nКількість введень =", count)
        break
    count += 1

# 28. Сума введень
# Просіть вводити числа до введення 0. Порахуйте і виведіть суму всіх введених чисел (без нуля).
# Підказка: Накопичуйте суму total += число на кожній ітерації.
print("\nСУМА ВВЕДЕНЬ")

total = 0
while True:
    n = int(input("Введіть ЦІЛЕ невід'ємне число: "))
    if n == 0:
        print("Програму завершено!\nСума введених чисел =", total)
        break
    total += n

# 29. Вгадай число
# Програма «загадує» число від 1 до 100 (задайте у коді).
# Користувач вводить здогадки, отримуючи підказки «більше» або «менше». Виводьте кількість спроб.
# Підказка: Для випадкового числа можна використати import random та random.randint(1, 100).
print("\nВГАДАЙ ЧИСЛО")

from random import randint

secret = randint(1, 100)

num_attempts = 0

while True:
    guess = int(input("Спробуйте вгадати число (від 1 до 100): "))
    num_attempts += 1

    if guess == secret:
        print("ВІТАЮ!\nВи вгадали число!\nКількість спроб:", num_attempts)
        num_attempts += 1
        break

    elif guess > secret:
        print("Підказка: загадане число менше!\n")
    else:
        print("Підказка! Загадане число більше!\n")

# 30. Таблиця множення (while)
# Введіть число N. За допомогою while виведіть таблицю множення для цього числа від 1 до 10.
# Підказка: Виводьте рядки виду: "N * i = результат".
print("\nТАБЛИЦЯ МНОЖЕННЯ")

n = int(input("Введіть число від 1 до 10: "))
i = 1

while i <= 10:
    print(f"Таблиця множення від {n} до 10: {n} * {i} = {n * i}")

    i += 1

# --- ЦИКЛ for ---

# 31. Числа від 1 до 100
# За допомогою циклу for виведіть усі числа від 1 до 100.
# Підказка: Використайте range(1, 101).
print("\nЧИСЛА від 1 до 100")

for i in range(1, 101):
    print("Числа від 1 до 100:", i)

# 32. Парні числа до 100
# За допомогою for виведіть усі парні числа від 1 до 100.
# Підказка: Використайте range(2, 101, 2) або перевірку n % 2 == 0.
print("\nПАРНІ ЧИСЛА до 100")

for i in range(2, 100 + 1, 2):
    print("Парні числа до 100:", i)

# 33. Непарні числа до 100
# За допомогою for виведіть усі непарні числа від 1 до 100.
# Підказка: Використайте range(1, 101, 2) або перевірку n % 2 != 0.
print("\nНЕ ПАРНІ ЧИСЛА до 100")

for i in range(1, 101, 2):
    print("Не парні числа до 100:", i)

# 34. Сума від 50 до 100
# За допомогою for обчисліть суму всіх цілих чисел від 50 до 100 включно.
# Підказка: range(50, 101) — правий кінець не включається.
print("\nСУМА від 50 до 100")

total = 0
for i in range(50, 101):
    total += i
print("Сума = ", total)

# 35. Сума квадратів
# Введіть число N. Обчисліть суму квадратів чисел від 1 до N: 1² + 2² + ... + N².
# Підказка: Додавайте i**2 на кожному кроці циклу.
print("\nСУМА КВАДРАТІВ")

N = int(input("Введіть число N: "))

total_sum = 0

for i in range(1, N + 1):
    total_sum += i ** 2

print(f"Сума квадратів чисел від 1 до {N} дорівнює: {total_sum}")

# 36. Степені двійки
# Введіть число N. Виведіть усі степені двійки від 2⁰ до 2^N.
# Підказка: Виводьте 2**i для i від 0 до N включно.
print("\nСТЕПЕНІ ДВІЙКИ")

n = int(input("Введіть число N: "))

for i in range(n + 1):
    print(f"2 у ^{i} степні = {2 ** i}")

# 37. Кратні числа
# За допомогою for порахуйте, скільки чисел від 1 до 100 кратні 7.
# Підказка: Умова кратності: n % 7 == 0. Використайте лічильник.
print("\nКРАТНІ ЧИСЛА")

counter = 0

for i in range(1, 101):
    if i % 7 == 0:
        counter += 1
    print("Кількість чисел кратних 7 =", counter)

# 38. Таблиця множення 1–10
# Виведіть повну таблицю множення від 1 до 10 у вигляді рядків: "i * j = результат".
# Підказка: Зовнішній цикл — множник i (1–10), внутрішній — множник j (1–10). Але для цього
# завдання достатньо одного циклу (обирайте самі).
print("\nТАБЛИЦЯ МНОЖЕННЯ")

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}")
    print()

# 39. Квадрат із символів
# Введіть розмір N. Намалюйте квадрат N×N із символів *.
# Підказка: Виводьте рядок з N зірочок N разів: print("*" * N).
print("\nКВАДРАТ ІЗ СИМВОЛІВ")

N = int(input("Введіть розмір N для квадрату: "))

for i in range(N):
    print('*  ' * N)

# 40. Прямокутник
# Введіть ширину та висоту. Намалюйте прямокутник відповідного розміру із символів *.
# Підказка: Зовнішній цикл — рядки (висота), виводьте рядок з ширина зірочок.
print("\nПРЯМОКУТНИК")

width = int(input("Введіть ширину прямокутника: "))
height = int(input("Введіть висоту прямокутника: "))

for i in range(1, width):
    print(height * "  *")

# --- ВКЛАДЕНІ ЦИКЛИ ---
# 41. Трикутник зі зірочок
# Виведіть прямокутний трикутник із символів *: перший рядок — 1 зірочка, другий — 2, і так далі до N.
# Підказка: for i in range(1, N+1): print("*" * i).
print("\nТРИКУТНИК ІЗ ЗІРОЧОК")

height = int(input("Введіть висоту трикутника: "))
for i in range(1, height + 1):
    print("* " * i)

# 42. Перевернутий трикутник
# Введіть N. Виведіть трикутник у зворотному порядку: перший рядок — N зірочок,
# останній — 1.
# Підказка: for i in range(N, 0, -1): print("*" * i).
print("\nПЕРЕВЕРНУТИЙ ТРИКУТНИК ІЗ ЗІРОЧОК")

width = int(input("Введіть ширину трикутника: "))
for i in range(width, 0, -1):
    print("* " * i)

# 43. Ялинка
# Виведіть ялинку: кожен рядок центрований і містить непарну кількість зірочок (1, 3, 5, ...).
# Підказка: Ширина рядка i = 2*i-1 зірочок, відступ = N-i пробілів.
print("\nЯЛИНКА ІЗ ЗІРОЧОК")
height = int(input("Введіть висоту ялинки: "))

# Зовнішній цикл відповідає за кожен рядок
for j in range(height - i):
    print(" ", end="")

    for k in range(2 * i - 1):
        print("*", end="")

        print()
    print("* " * i)

# 44. Таблиця множення 10×10
# Виведіть повну таблицю множення від 1 до 10 у вигляді сітки (рядки і стовпці).
# Підказка: Два вкладені цикли for i in range(1,11) і for j in range(1,11). Форматуйте вивід
# через f-string або .format().


# 45. Усі пари чисел
# Виведіть усі можливі пари (i, j), де i та j — числа від 1 до 5.
# Підказка: Два вкладені цикли; виводьте кожну пару у форматі "(i, j)".


# 46. Дільники числа
# Введіть число N. Знайдіть і виведіть усі його дільники (числа, на які N ділиться без остачі).
# Підказка: Перевіряйте N % i == 0 для i від 1 до N.


# 47. Просте число
# Введіть число N. Визначте, чи є воно простим, і виведіть відповідь.
# Підказка: Просте число ділиться лише на 1 і на себе. Перевіряйте дільники від 2 до N-1 або до sqrt(N).


# 48. Прості числа до N
# Введіть число N. Виведіть усі прості числа від 2 до N.
# Підказка: Для кожного числа від 2 до N перевіряйте простоту вкладеним циклом або алгоритмом решета Ератосфена.


# 49. Шахова дошка
# Виведіть шахову дошку 8×8 із символів # та пробілу, що чергуються.
# Підказка: Якщо сума (i + j) парна — виводьте "#", інакше — " " (або навпаки).


# 50. Числовий трикутник
# Введіть N. Виведіть трикутник, де в i-му рядку знаходяться числа від 1 до i.
# Підказка: Рядок 1: "1", рядок 2: "1 2", рядок 3: "1 2 3" тощо.


# --- РЯДКИ ---
# 51. Символи на окремих рядках
# Введіть рядок. Виведіть кожен символ на окремому рядку.
# Підказка: Ітеруйте по рядку: for ch in text: print(ch).
print("\nСИМВОЛИ НА ОКРЕМИХ РЯДКАХ")
text = input("Enter string: ")

for char in text:
    print("Individual characters: ", char)

# 52. Довжина рядка
# Введіть рядок. Порахуйте і виведіть кількість символів у ньому без використання len().
# Підказка: Використайте лічильник і цикл for.
print("\nДОВЖИНА РЯДКА")

text = input("Enter string: ")
i = 0

for char in text:
    i = i + 1
print("Number of characters: ", i)

# 53. Кількість голосних
# Введіть рядок. Порахуйте кількість голосних літер (a, e, i, o, u та їх українські відповідники).
# Підказка: Перевіряйте ch.lower() in "аеиіоуяюєїaeiou".
print("\nКІЛЬКІСТЬ ГОЛОСНИХ")

text = input("Enter string: ")
counter = 0

for char in text:
    if char.lower() in "аеиіоуяюєїaeiou":
        counter = counter + 1
print("Number of vowels: ", counter)

# 54. Кількість пробілів
# Введіть рядок. Порахуйте і виведіть кількість пробілів у ньому.
# Підказка: Перевіряйте ch == " " або використайте text.count(" ").
print("\nКІЛЬКІСТЬ ПРОБІЛІВ")

text = input("Enter string: ")
counter = 0

for char in text:
    if char.lower() in "аеиіоуяюєїaeiou":
        counter = counter + 1
print("Number of vowels: ", counter)

# 55. Наявність слова Python
# Введіть рядок. Перевірте, чи містить він слово "Python", і виведіть відповідь.
# Підказка: Використайте оператор in: "Python" in text.
print("\nНАЯВНІСТЬ СЛОВА 'Python'")

text = input("Lookin for the word 'Python': ")

if "Python" in text:
    print("У введеному тексті є слово Python.\n The word 'Python' is in the text entered")
else:
    print("У введеному тексті немає слова 'Python'!\n The word 'Python' is not in the text entered")

# 56. Заміна пробілів
# Введіть рядок. Замініть у ньому всі пробіли символом "_" і виведіть результат.
# Підказка: Використайте метод text.replace(" ", "_").
print("\nЗАМІНА ПРОБІЛІВ")

text = input("Enter string: ")

text_correct = text.replace(" ", "_")
print("Текст без пробілів\n Text without spaces: ", text_correct)

# 57. Верхній регістр
# Введіть рядок. Перетворіть усі літери у верхній регістр і виведіть результат.
# Підказка: Використайте метод text.upper().
print("\nВЕРХНІЙ РЕГІСТР")

text = input("Enter string: ")

text_origin = text
text_upper = text.upper()

print("Оригінальний текст / Text without spaces: ", text_origin)
print("\nТекст ВЕЛИКИМИ літерами / Text with spaces: ", text_upper)

# 58. Нижній регістр
# Введіть рядок. Перетворіть усі літери у нижній регістр і виведіть результат.
# Підказка: Використайте метод text.lower().
print("\nНИЖНІЙ РЕГІСТР")

text = input("Enter string: ")

text_origin = text
text_lowercase = text.lower()

print("Оригінальний текст / Text without spaces: ", text_origin)
print("\nТекст ВЕЛИКИМИ літерами / Text with spaces: ", text_lowercase)

# 59. Паліндром
# Введіть рядок. Визначте, чи є він паліндромом (читається однаково з обох боків).
# Ігноруйте регістр і пробіли.
# Підказка: Очістіть рядок: s = text.lower().replace(" ",""). Порівняйте s == s[::-1].
print("\nПОЛІНДРОМ")

text = input("Enter string: ")
clean_text = text.lower().replace(" ", "")

if clean_text == clean_text[::-1]:
    print("Введений текст є Поліндромом")
else:
    print("Введений текст не є Поліндромом")

# 60. Кількість входжень літери
# Введіть рядок і окрему літеру. Порахуйте і виведіть, скільки разів ця літера зустрічається в рядку.
# Підказка: Використайте text.lower().count(letter.lower()).
print("\nКІЛЬКІСТЬ ВХОДЖЕНЬ ЛІТЕРИ")

text = input("Enter string: ")
input_letters = input("Enter letter: ").lower()

count_letter = text.lower().count(input_letters)

print(f"The Letter '{input_letters}' occurs {count_letter} times")

# --- СПИСКИ ---

# 61. Список із 10 чисел
# Попросіть користувача ввести 10 чисел і збережіть їх у список. Виведіть список.
# Підказка: Використайте цикл і метод .append() або list comprehension.
print("\nСПИСОК ІЗ 10 ЧИСЕЛ")

user_input = input("Enter 10 any numbers: ").split()

num_list = []

for num in user_input:
    number_int = int(num)  # перетворюємо введений текст на число
    num_list.append(number_int)  # додаємо число в числовий список
print("You have entered a list of numbers: ", *num_list)  # вивід з розпаковкой *

# 62. Сума елементів списку
# Маючи список чисел, обчисліть і виведіть суму всіх його елементів без використання sum().
# Підказка: Ітеруйте по списку і накопичуйте суму у змінній total.
print("\nСУМА ЕЛЕМЕНТІВ СПИСКУ")

user_input = input("Enter 10 any numbers: ").split()

total = 0

for num in user_input:
    number_int = int(num)  # перетворюємо введений текст на число
    total += number_int  # додаємо число до загальної суми
print("Sum of all numbers: ", total)

# 63. Найбільший елемент
# Знайдіть і виведіть найбільший елемент списку без використання max().
# Підказка: Ініціалізуйте maximum = lst[0], порівнюйте з кожним наступним елементом.
print("\nНАЙБІЛЬШИЙ ЕЛЕМЕНТ")

user_input = input("Enter any numbers: ").split()

# Перетворюємо весь список текстів на список СПРАВЖНІХ чисел
numbers = []
for num in user_input:
    numbers.append(int(num))

# назначаємо найперше число, як стартовий максимум
maximum = numbers[0]

# Порівнюємо максимум з кожним числом у списку
for current_numbers in numbers:
    if current_numbers > maximum:  # Якщо поточне число більше за 'maximum'
        maximum = current_numbers  # - то воно стає новим 'maximum'
print("The largest element in the list: ", maximum)

# 64. Найменший елемент
# Знайдіть і виведіть найменший елемент списку без використання min().
# Підказка: Аналогічно до пошуку максимуму, але з умовою el < minimum.
print("\nНАЙМЕНШИЙ ЕЛЕМЕНТ")

user_input = input("Enter any numbers: ").split()

# Перетворюємо весь список текстів на список СПРАВЖНІХ чисел
numbers = []
for num in user_input:
    numbers.append(int(num))

# назначаємо найперше число, як стартовий мінімум
minimum = numbers[0]

# Порівнюємо мінімум з кожним числом у списку
for current_numbers in numbers:
    if current_numbers < minimum:  # Якщо поточне число більше за 'minimum'
        minimum = current_numbers  # - то воно стає новим 'minimum'
print("The largest element in the list: ", minimum)

# 65. Середнє значення
# Обчисліть і виведіть середнє арифметичне елементів списку.
# Підказка: Середнє = сума елементів / кількість елементів. Кількість — len(lst).
print("\nСЕРЕДНЄ ЗНАЧЕННЯ")

user_input = input("Enter any numbers: ").split()

# Перетворюємо введені текстові елементи на список чисел
numbers = []

for num in user_input:
    numbers.append(int(num))

# Рахуємо суму всіх елементів
total_sum = 0

for num in numbers:
    total_sum += num

# Дізнаємося кількість елементів у списку
count = len(numbers)

if count > 0:
    average = total_sum / count
    print("Average value: ", total)
else:
    print("The list is empty")

# 66. Список квадратів
# Створіть список квадратів чисел від 1 до 10: [1, 4, 9, ..., 100].
# Підказка: Використайте list comprehension: [i**2 for i in range(1, 11)].
print("\nСПИСОК КВАДРАТІВ ЧИСЕЛ")

square = [i ** 2 for i in range(1, 11)]
print("Square of numbers", square)

# 67. Лише парні числа
# Маючи список чисел, створіть новий список, що містить лише парні елементи вихідного.
# Підказка: Використайте list comprehension: [x for x in lst if x % 2 == 0].
print("\nПАРНІ ЧИСЛА")

user_input = input("Enter any numbers: ").split()

numbers = [int(num) for num in user_input]

even = [i for i in numbers if i % 2 == 0]

print("Even numbers", even)

# 68. Видалення від'ємних
# Маючи список чисел, видаліть із нього всі від'ємні значення. Виведіть очищений список.
# Підказка: Створіть новий список: [x for x in lst if x >= 0], або видаляйте елементи через remove().
print("\nВИДАЛЕННЯ ВІД'ЄМНИХ")
user_input = input("Enter any numbers: ").split()

numbers = [int(i) for i in user_input]

positive_numbers = [i for i in numbers if i >= 0]

print("Output is positive numbers: ", positive_numbers)

# 69. Кількість додатних
# Порахуйте, скільки елементів у списку є додатними (більшими за нуль).
# Підказка: Використайте лічильник або sum(1 for x in lst if x > 0).
print("\nКІЛЬКІСТЬ ДОДАТНИХ")
user_input = input("Enter any numbers: ").split()

numbers = [int(i) for i in user_input]

# створюємо список з фільтром додатних чисел > 0
positive_only = [x for x in numbers if x > 0]

count_numbers = len(positive_only)

print("Count of positive numbers: ", count_numbers)

# 70. Перший і останній
# Поміняйте місцями перший і останній елементи списку. Виведіть результат.
# Підказка: lst[0], lst[-1] = lst[-1], lst[0] — Python дозволяє таке присвоєння.
print("\nПЕРШИЙ І ОСТАННІЙ")
user_input = input("Enter any numbers: ").split()

numbers = [int(i) for i in user_input]

numbers[0], numbers[-1] = numbers[-1], numbers[0]

print("Replacing the first and last element: ", numbers)

# --- РОБОТА ЗІ СПИСКАМИ РЯДКІВ ---
# 71. Довгі слова
# Маючи список слів, виведіть лише ті, довжина яких перевищує 5 символів.
# Підказка: Умова фільтрації: len(word) > 5.
print("\nДОВГІ СЛОВА")
word_input = input("Enter a list of words: ").split()

list_words = [word for word in word_input if len(word_input) > 5]

print("List of words 5+ characters: ", list_words)

# 72. Найдовше слово
# Знайдіть і виведіть найдовше слово зі списку без використання max().
# Підказка: Ітеруйте і порівнюйте len(word) з довжиною поточного максимуму.
print("\nНАЙДОВШЕ СЛОВО")
word_input = input("Enter a list of words: ").split()

longest_words = word_input[0]

for word in word_input:
    if len(word) > len(longest_words):
        longest_words = word

print("The longest word is: ", longest_words)

# 73. Найкоротше слово
# Знайдіть і виведіть найкоротше слово зі списку без використання min().
# Підказка: Аналогічно до пошуку найдовшого, але порівнюйте на менше.
print("\nНАЙКОРОТШЕ СЛОВО")
word_input = input("Enter a list of words: ").split()

shortest_words = word_input[0]

for word in word_input:
    if len(word) < len(shortest_words):
        shortest_words = word

print("The longest word is: ", shortest_words)

# 74. Слова з великої літери
# Виведіть лише ті слова зі списку, що починаються з великої літери.
# Підказка: Метод word[0].isupper() або word.istitle().
print("\nСЛОВА з ВЕЛИКОЇ ЛІТЕРИ")
word_input = input("Enter a list of words: ").split()

capitalized_words = [word for word in word_input if word.istitle()]

print("Word starting with a capital letter: ", capitalized_words)

# 75. Слова з літерою а
# Виведіть слова зі списку, що містять літеру "а" (в будь-якому регістрі).
# Підказка: Умова: "а" in word.lower().
print("\nСЛОВО з ЛІТЕРОЮ 'а' ")
word_input = input("Enter a list of words: ").split()

words_a = [word for word in word_input if "a" in word.lower() or "а" in word.lower()]

print("Words is a letter 'a': ", words_a)

# 76. Слова на -ія
# Виведіть слова зі списку, що закінчуються на "ія".
# Підказка: Метод word.endswith("ія").
print("\nСЛОВА ЗАКІНЧУЮТЬСЯ на 'ія' ")
word_input = input("Enter a list of words: ").split()

words_end = [word for word in word_input if word.lower().endswith("ія")]

print("Words ending in 'ія': ", words_end)

# 77. Сортування за алфавітом
# Відсортуйте список слів за алфавітом і виведіть результат.
# Підказка: Використайте sorted(lst) або lst.sort().
print("\nСОРТУВАННЯ ЗА АЛФАВІТОМ")
word_input = input("Enter a list of words: ").split()

words_alphabet = sorted(word_input)

print("Sorted words Alphabetically : ", words_alphabet)

# 78. Сортування за довжиною
# Відсортуйте список слів за зростанням їхньої довжини і виведіть.
# Підказка: sorted(lst, key=len) або lst.sort(key=len).
print("\nСОРТУВАННЯ ЗА ДОВЖИНОЮ")
word_input = input("Enter a list of words: ").split()

words_leng = sorted(word_input, key=len)

print("Sorted words Alphabetically : ", words_leng)

# 79. Кількість слів
# Порахуйте та виведіть кількість слів у списку.
# Підказка: Просто len(lst).
print("\nКІЛЬКІСТЬ СЛІВ")
word_input = input("Enter a list of words: ").split()

words_num = len(word_input)

print("Number of words in the list: ", words_num)

# 80. Верхній регістр
# Створіть новий список, де всі слова записані у верхньому регістрі.
# Підказка: List comprehension: [w.upper() for w in lst].
print("\nСЛОВА у ВЕРХНЬОМУ РЕГІСТРІ")
word_input = input("Enter a list of words: ").split()

words_upper = [word.upper() for word in word_input]

print("Capitalized words: ", words_upper)

# --- ФУНКЦІЇ ---
# 81. Квадрат числа
# Напишіть функцію square(n), яка приймає число і повертає його квадрат.
# Викличте і виведіть результат.
# Підказка: return n ** 2
print("\nКВАДРАТ ЧИСЛА")


def square(n):
    return n ** 2


user_input_num = int(input("Enter any numbers: "))

func = square(user_input_num)

print(f"Square of a number '{user_input_num}' =  {func} ")

# 82. Куб числа
# Напишіть функцію cube(n), яка приймає число і повертає його куб.
# Викличте і виведіть результат.
# Підказка: return n ** 3
print("\nКУБ ЧИСЛА")


def cube(n):
    return n ** 3


input_num = int(input("Enter any numbers: "))

func = cube(input_num)

print(f"Cube of a number '{input_num}' =  {func} ")

# 83. Перевірка парності
# Напишіть функцію is_even(n), яка повертає True, якщо число парне, і False — якщо непарне.
# Підказка: return n % 2 == 0
print("\nПЕРЕВІРКА ПАРНОСТІ")


def is_even(n):
    return n % 2 == 0


input_num = int(input("Enter any numbers: "))
func = is_even(input_num)

print(f"Is the number '{input_num}' even?: {func}")

# 84. Максимум з двох
# Напишіть функцію max_two(a, b), яка повертає більше з двох чисел без використання  max().
# Підказка: return a if a > b else b
print("\nМАКСИМУМ з ДВОХ")


def max_two(a, b):
    return a if a > b else b


user_input = input("Enter any numbers: ").split()

num1 = int(user_input[0])
num2 = int(user_input[1])

func_result = max_two(num1, num2)

print(f"The maximum of '{num1}' and '{num2}' is: {func_result}")

# 85. Максимум з трьох
# Напишіть функцію max_three(a, b, c), яка повертає найбільше з трьох чисел.
# Підказка: Порівнюйте попарно або викличте max_two двічі.
print("\nМАКСИМУМ з ТРЬОХ")


def max_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


user_input = input("Enter any numbers: ").split()

num1 = int(user_input[0])
num2 = int(user_input[1])
num3 = int(user_input[2])

func_result = max_three(num1, num2, num3)

print(f"The maximum of '{num1}' '{num2}' and '{num3}' is: {func_result}")

# 86. Кількість голосних
# Напишіть функцію count_vowels(text), яка приймає рядок і повертає кількість голосних у ньому.
# Підказка: Ітеруйте і перевіряйте ch.lower() in "аеиіоуяюєїaeiou".
print("\nКІЛЬКІСТЬ ГОЛОСНИХ")


def count_vowels(text):
    count = 0

    for x in text:
        if x.lower() in "аеиіоуяюєїaeiou":
            count += 1
    return count


user_text = input("Enter any text: ")

func_result = count_vowels(user_text)

print(f"Count vowels of text '{user_text}' is: {func_result}")

# 87. Перевірка паліндрома
# Напишіть функцію is_palindrome(text), яка повертає True, якщо рядок є паліндромом.
# Підказка: s = text.lower().replace(" ",""); return s == s[::-1]
print("\nПЕРЕВІРКА ПАЛІНДРОМА")


def is_palindrome(text):
    s = text.lower().replace(" ", "")
    return s == s[::-1]


user_text = input("Enter any text: ")

func_result = is_palindrome(user_text)

if func_result:
    print(f"YES, the text '{user_text}' is a PALINDROME!")
else:
    print(f"NO, the text '{user_text}' is NOT a palindrome.")

# 88. Список парних
# Напишіть функцію get_evens(lst), яка приймає список чисел і повертає новий список лише з парними.
# Підказка: return [x for x in lst if x % 2 == 0]
print("\nСПИСОК ПАРНИХ")


def get_evens(lst):
    return [x for x in lst if x % 2 == 0]


user_input = input("Enter any numbers: ").strip().split()
user_numbers = [int(i) for i in user_input]

func_result = get_evens(user_numbers)

print(f"The list evens numbers: ", *func_result)

# 89. Фільтрація за довжиною
# Напишіть функцію filter_by_length(words, n), яка повертає слова довжиною більше n символів.
# Підказка: return [w for w in words if len(w) > n]
print("\nФІЛЬТРАЦІЯ ЗА ДОВЖИНОЮ")


def filter_by_length(words, n):
    return [w for w in words if len(w) > n]


user_text = input("Enter any text: ").split()

func_result = filter_by_length(user_text, 3)

print("Words longer than 3 characters:", func_result)

# 90. Слова з символом
# Напишіть функцію words_with_char(words, ch), яка повертає список слів, що містять заданий символ.
# Підказка: return [w for w in words if ch.lower() in w.lower()]
print("\nСЛОВА З СИМВОЛОМ")


def words_with_char(words, ch):
    return [w for w in words if ch.lower() in w.lower()]


user_text = input("Enter any text: ").split()
user_char = input("Enter a character to search for words: ")

func_result = words_with_char(user_text, user_char)

print("Words longer than 3 characters:", func_result)

# --- СЛОВНИКИ ---
# 91. Словник учня
# Створіть словник з даними учня: ключі "ім'я", "вік", "клас". Виведіть кожне поле окремим рядком.
# Підказка: Зверніться до значень через student["ім'я"] тощо.
print("\nСЛОВНИК УЧНЯ")

students = {
    "Name": "Valerii",
    "Age": "8",
    "Class": "2-B"
}
print("Student's name:", students["Name"])
print("Student's age:", students["Age"])
print("Student's class:", students["Class"])

# 92. Всі ключі
# Маючи довільний словник, виведіть усі його ключі.
# Підказка: Використайте dict.keys() або ітеруйте: for key in d.
print("\nВИВЕДЕННЯ ВСІХ КЛЮЧІВ")

students = {
    "Name": "Valerii",
    "Age": "8",
    "Class": "2-B"
}
print("Спосіб 1 (через .keys()):")
print(students.keys())

print("Спосіб 2 (через ітерацію for key in d:")
for key in students:
    print(key)

# 93. Всі значення
# Маючи довільний словник, виведіть усі його значення.
# Підказка: Використайте dict.values().
print("\nВИВЕДЕННЯ ВСІХ ЗНАЧЕНЬ")

students = {
    "Name": "Valerii",
    "Age": "8",
    "Class": "2-B"
}
for value in students.values():
    print(value)

# 94. Додавання елемента
# Маючи словник, додайте до нього новий ключ-значення. Виведіть оновлений словник.
# Підказка: d["новий_ключ"] = "значення"
print("\nДОДАВАННЯ ЕЛЕМЕНТА")

student = {
    "Name": "Valerii",
    "Age": 8,
    "Class": "2-B",
    }
student["School"] = "№3"
print(student)

# 95. Видалення елемента
# Маючи словник, видаліть із нього елемент за ключем. Виведіть оновлений словник.
# Підказка: del d["ключ"] або d.pop("ключ").
print("\nВИДАЛЕННЯ ЕЛЕМЕНТА")

student = {
    "Name": "Valerii",
    "Age": 8,
    "Class": "2-B",
    }
student["School"] = "№3"
print(student)

# 96. Перевірка ключа
# Введіть ключ з клавіатури. Перевірте, чи є він у словнику, і виведіть відповідь.
# Підказка: Використайте оператор in: "ключ" in d.
print("\nПЕРЕВІРКА КЛЮЧА")

student = {
    "Name": "Valerii",
    "Age": 8,
    "Class": "2-B",
    "School": "№3"
    }

user_key = input("Введіть ключ для перевірки: ")
if user_key in student:
    print("YES, such a key is in the dictionary")
else:
    print("NO, such a key is not in the dictionary")

# 97. Значення за ключем
# Введіть ключ. Знайдіть та виведіть відповідне значення або повідомлення "не знайдено".
# Підказка: Використайте d.get("ключ", "не знайдено").
print("\nЗНАЧЕННЯ ЗА КЛЮЧЕМ")

student = {
    "Name": "Valerii",
    "Age": 8,
    "Class": "2-B",
    "School": "№3"
    }

user_key = input("Введіть ключ для перевірки: ")
result = students.get(user_key, "не знайдено")

print(result)

# 98. Оновлення значення
# Маючи словник, змініть значення одного з ключів на нове. Виведіть оновлений словник.
# Підказка: d["ключ"] = нове_значення
print("\nОНОВЛЕННЯ ЗНАЧЕННЯ")

student = {
    "Name": "Valerii",
    "Age": 8,
    "Class": "2-B",
    "School": "№3"
    }

student["School"]="№1"

print("Update dictionary", student)

# 99. Кількість елементів
# Виведіть кількість пар ключ-значення у словнику.
# Підказка: len(d) повертає кількість елементів.
print("\nКІЛЬКІСТЬ ЕЛЕМЕНТІВ")

student = {
    "Name": "Valerii",
    "Age": 8,
    "Class": "2-B",
    "School": "№3"
    }
length_student = len(student)

print("Number of key-value pairs in the dictionary =", length_student)

# 100. Міні словник перекладу
# Створіть словник, де ключі — слова однією мовою, значення — їх переклад.
# Введіть слово і виведіть переклад або "слово не знайдено".
# Підказка: d = {"кіт": "cat", "собака": "dog", ...}. Використайте d.get(word, "не знайдено").
print("\nМІНІ СЛОВНИК ПЕРЕКЛАДУ")

translate_dict = {
    "собака": "Dog",
    "кіт": "Cat",
    "людина": "Person",
    "кінь": "Horse",
    "автомобіль": "Car",
    }

user_key = input("Введіть слово для перекладу: ").lower()
result = translate_dict.get(user_key, "таке слово не знайдено")

print(result)

    # ---- ЧАСТИНА 2. ОБ'ЄКТНО-ОРІЄНТОВНЕ ПРОГРАМУВАННЯ (ООП)
    # --- Рівень 1. Один клас ---

# 1. Клас Student — інформація про студента
# Атрибути: ім'я (str), вік (int), середній бал (float).
# Метод display(): виводить усі дані про студента у зручному форматі.
# Метод update_grade(new_grade): приймає нове значення балу і оновлює атрибут.
# Перевіряйте, що бал у межах 0–100.
print("\n/ООП/ ІНФОРМАЦІЯ ПРО СТУДЕНТА")
class Student:
    def __init__(self, name:str, age:int, average_grade:float):
        self.name = name
        self.age = age
        self.average_grade = average_grade

    def display(self):
        print(f"Student: {self.name} | Age: {self.age} | Average Grade: {self.average_grade}")

    def update_grade(self, new_grade:float):
        if 0 <= new_grade <= 100:
            self.average_grade = new_grade
            print(f"Score for {self.name} successfully update to: {self.average_grade}")
        else:
            print("Error! Score must be between 0 and 100")

# РОБОТА КЛАСУ
# Створюємо об'єкт студента
student1 = Student("Valerii", 19, 85.5)

# Виводимо початкові дані
student1.display()

# Пробуємо поставити неправильний бал (спрацює помилка)
student1.update_grade(150)

# Оновлюємо бал правильним значенням
student1.update_grade(95.0)

# Виводимо оновлені дані, щоб перевірити результат
student1.display()


# 2. Клас Book — книга
# Атрибути: назва (str), автор (str), кількість сторінок (int).
# Метод display(): виводить назву, автора та кількість сторінок.
# Метод update_pages(n): оновлює кількість сторінок. Перевіряйте, що n > 0.
print("\n/ООП/ КНИГА")
class Book:
    def __init__(self, name:str, author:str, page:int):
        self.name = name
        self.author = author
        self.page = page

    def display(self):
        print(f"Book: {self.name} | Author: {self.author} | Count page: {self.page}")

    def update_pages(self, num:float):
        if num > 0:
            self.page = num
            print(f"Кількість сторінок для  '{self.name}' оновлено до: {self.page}")
        else:
            print("Помилка! Кількість сторінок повинна бути більше '0'!")

# РОБОТА КЛАСУ
# Створюємо об'єкт книги
my_book = Book("Kobzar", "Taras Shevchenko", 454)

# Виводимо початкову інформацію
my_book.display()

# Пробуємо поставити неправильний бал (спрацює помилка)
my_book.update_pages(-15)

# Оновлюємо бал правильним значенням
my_book.update_pages(450)

# Виводимо оновлені дані, щоб перевірити результат
my_book.display()


# 3. Клас Dog — собака
# Атрибути: кличка (str), порода (str), вік у роках (int).
# Метод display(): виводить усі дані про собаку.
# Метод birthday(): збільшує вік на 1 рік і виводить привітання.
print("\n/ООП/ Dog-Собака")
class Dog:
    def __init__(self, nickname:str, dog_breed:str, age:int):
        self.nickname = nickname
        self.dog_breed = dog_breed
        self.age = age

    def display(self):
        print(f":Dog's nickname: '{self.nickname}' | Dog breed: '{self.dog_breed}' | Age: {self.age}")

    def birthday(self):
        self.age += 1
        print(f"Happy Birhday '{self.nickname}' you are: {self.age} yeras old")

# --- РОБОТА КЛАСУ ---
# 1. Створюємо об'єкт собаки
my_dog = Dog("Рекс", "Німецька вівчарка", 3)

# 2. Виводимо початкову інформацію
my_dog.display()

# 3. Святкуємо день народження (вік збільшиться з 3 до 4)
my_dog.birthday()

# 4. Виводимо оновлені дані для перевірки
my_dog.display()

# 4. Клас Product — товар
# Атрибути: назва (str), ціна (float), кількість на складі (int).
# Метод display(): виводить повну інформацію про товар.
# Метод set_price(new_price): оновлює ціну. Ціна не може бути від'ємною.
# Метод restock(amount): додає кількість одиниць на склад.
print("\n/ООП/ Dog-Собака")
class Product:
    def __init__(self, product_name:str, price:float, count:int):
        self.product_name = product_name
        self.price = price
        self.count = count

    def display(self):
        print(f":Product name: '{self.product_name}' | Price: '{self.price}' | Count: {self.count}")

    def set_price(self, new_price:float):
        if new_price >= 0:
            self.price = new_price
            print(f"Price for '{self.product_name}' update: {self.price} hrn")
        else:
            print("Error! Price cannot in negative")

    def restock(self, amount:int):
        if amount > 0:
            self.count += amount
            print(f"Added to stock {amount} pieces. Товар: '{self.product_name}'")
        else:
            print("Error! The quantity to add must be greater then '0'.")

# --- РОБОТА КЛАСУ ---
# 1. Створюємо об'єкт продукту
func_prod = Product("TP-Link Archer 17", "1800", 3)

# 2. Виводимо початкову інформацію
func_prod.display()

# 3. Тестуємо заміну ціни (помилкову)
func_prod.set_price(-10)

# 4. Тестуємо заміну ціни (ПРАВИЛЬНУ)
func_prod.set_price(2000.99)

# 5. Тестуємо заповнення складу
func_prod.restock(4)

# 5. Вивід результату
func_prod.display()

# 5. Клас Movie — фільм
# Атрибути: назва (str), жанр (str), рейтинг (float, від 0 до 10).
# Метод display(): виводить усі дані про фільм.
# Метод update_rating(r): оновлює рейтинг. Перевіряйте діапазон 0–10.
print("\n/ООП/ Movie-фільм")

class Movie:
    def __init__(self, name_movie: str, genre: str, rating: float):
        self.name_movie = name_movie
        self.genre = genre
        self.rating = rating

    def display(self):
        print(f":Name Movie: '{self.name_movie}' | Genre: '{self.genre}' | Rating: {self.rating}")

    def update_rating(self, new_rating: float):
        if 0 <= new_rating <= 10:
            self.rating = new_rating
            print(f"Movie rating '{self.name_movie}' update to {self.rating}")
        else:
            print(f"Error! Rating '{self.name_movie}' must be between 0 and 10. No changes made")

# --- Перевірка РОБОТИ КЛАСУ ---
if __name__ == "__main__":
    # 1. Створюємо об'єкт фільму
    my_movie = Movie("Game Of Thrones", "Epic fantasy", 9.0)
    my_movie.display()

    # 2. Спробуємо оновити рейтинг на коректний
    my_movie.update_rating(9.2)
    my_movie.display()

    # 3. Спробуємо ввести некоректний рейтинг
    my_movie.update_rating(12.5)
    my_movie.display()


    # --- Рівень 2. КЛАС З ДІЯМИ ---
# 6. Клас BankAccount — банківський рахунок
# Атрибути: номер рахунку (str), власник (str), баланс (float, за замовчуванням 0).
# Метод deposit(amount): поповнює баланс. Сума має бути більшою за 0.
# Метод withdraw(amount): знімає кошти. Забороняйте зняття більше, ніж є на рахунку.
# Метод get_balance(): виводить поточний баланс.
print("\n/ООП/ Клас Банківський рахунок")

class BankAccount:
    def __init__(self, account_number:str, owner:str, balance:float = 0.0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount:float):
        if amount > 0:
            self.balance += amount
            print(f"Ваш рахунок поповнено на {amount}. Баланс '{self.balance}'")
        else:
            print("Error! Amount can't be negative")

    def withdraw(self, amount:float):
        if amount > 0:
            self.balance -= amount
            print(f"Знято! Ваш баланс: '{self.balance}'")
        elif amount < 0:
            print("Сума знаття має бути більшою за 0")
        elif amount > self.balance:
            print("Введена сума більша за залишок на рахунку!")

    def get_balance(self):
        print(f"Поточний баланс на рахунку- {self.account_number} : {self.balance}")
        return self.balance

# --- Перевірка роботи ---
# Створюємо рахунок (баланс буде 0 за замовчуванням)
my_account = BankAccount("UA1510", "Valerii")

my_account.get_balance()       # Виведе: 0.0
my_account.deposit(1500)        # Поповнить на 1500
my_account.withdraw(2000)       # Видасть помилку (недостатньо коштів)
my_account.withdraw(800)       # Зніме 800, залишиться 700
my_account.get_balance()       # Виведе: 700.0

# 7. Клас Rectangle — прямокутник
# Атрибути: ширина (float), висота (float).
# Метод area(): повертає площу: ширина * висота.
# Метод perimeter(): повертає периметр: 2 * (ширина + висота).
# Метод resize(w, h): змінює розміри. Обидва значення мають бути > 0.
print("\n/ООП/ Клас Rectangle — прямокутник")

class Rectangle:
    def __init__(self, width:float, height:float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def resize(self, w: float, h: float):
        if w > 0 and h > 0:
            self.width = w
            self.height = h
        else:
            print("Error! Width and height can't be greater than 0")

# --- Перевірка роботи Класу - ПРЯМОКУТНИК---
input_width = float(input("Enter the width of the rectangle: "))
input_height = float(input("Enter the height of the rectangle: "))

rect = Rectangle(input_width, input_height)

print(f"Area of a rectangle: {rect.area()}")
print(f"Perimeter of a rectangle: {rect.perimeter()}")

# 8. Клас Circle — коло
# Атрибути: радіус (float).
# Метод area(): повертає площу: π * r². Використайте math.pi.
# Метод circumference(): повертає довжину кола: 2 * π * r.
print("\n/ООП/ Клас Circle — коло")
import math

class Circle:
    def __init__(self, radius:float):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius

# --- Перевірка роботи Класу - КОЛО ---
input_radius = float(input("Enter the radius of the circle: "))
circle = Circle(input_radius)
print(f"Area of a circle: {circle.area():.2f}")
print(f"Length of a circle: {circle.circumference():.2f}")

# 9. Клас Employee — співробітник
# Атрибути: ім'я (str), посада (str), зарплата (float).
# Метод display(): виводить усі дані про співробітника.
# Метод raise_salary(percent): підвищує зарплату на заданий відсоток. Перевіряйте percent > 0.
print("\n/ООП/ Клас Employee — співробітник")

class Employee:
    def __init__(self, name: str, position: str, salary: float):
        self.name = name
        self.position = position
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}")

    def raise_salary(self, percent: float):
        if percent > 0:
            self.salary += self.salary * (percent / 100)
        else:
            print("Percentage must be greater than 0")

# --- Перевірка роботи Класу - Співробітник ---
worker = Employee("Valerii", "Manager", 40000)

print("Виводимо дані про співробітника!")
worker.display()

print("\n--- Спроба некоректного підвищення (-5%) ---")
worker.raise_salary(-5)

print("\n--- Підвищення зарплати на 10% ---")
worker.raise_salary(10)

# Виводимо оновлені дані
worker.display()


# 10. Клас Timer — таймер
# Атрибути: кількість секунд (int, за замовчуванням 0).
# Метод add(seconds): додає секунди. Значення має бути > 0.
# Метод subtract(seconds): віднімає секунди. Час не може стати від'ємним.
# Метод display(): виводить час у форматі "ГГ:ХХ:СС".
print("\n/ООП/ Клас Timer — таймер")

class Timer:
    def __init__(self, seconds: int = 0):
        self.seconds = max(0, seconds)

    def add(self, seconds: int):
        if seconds > 0:
            self.seconds += seconds
        else:
            print("Error! Seconds can't be negative")

    def subtract(self, seconds: int):
        if seconds > 0:
             # Час не може стати меншим за 0
            if self.seconds - seconds >= 0:
                self.seconds -= seconds
            else:
                self.seconds = 0
                print("Таймер скинуто до 0, час не може бути від'ємним!")
        else:
            print("Кількість секунд для віднімання має бути більшою за 0!")

    def display(self):
        # Переводимо загальні секунди у Години, Хвилини, Секунди
        hours = self.seconds // 3600
        minutes = (self.seconds % 3600) // 60
        secs = self.seconds % 60

    # Модифікатор :02d автоматично додає нуль попереду, якщо цифра однозначна (наприклад, 05 замість 5)
        print(f"Час: {hours:02d}:{minutes:02d}:{secs:02d}")

    # --- Перевірка роботи Класу - Таймер ---

    # 1. Створюємо таймер за замовчуванням (0 секунд)
my_timer = Timer()
print("Початковий стан:")
my_timer.display()

    # 2. Додаємо 4000 секунд (це 1 година, 6 хвилин і 40 секунд)
print("\nДодаємо 4000 секунд:")
my_timer.add(4000)
my_timer.display()

    # 3. Віднімаємо 500 секунд
print("\nВіднімаємо 500 секунд:")
my_timer.subtract(500)
my_timer.display()

    # 4. Пробуємо відняти забагато часу
print("\nСпроба відняти 5000 секунд (більше, ніж є):")
my_timer.subtract(5000)
my_timer.display()

    # --- Рівень 3. КЛАС МІСТИТЬ СПИСОК ОБ'ЄКТІВ ---
# 11. Клас Library — бібліотека
# Клас Book: атрибути — назва (str), автор (str).
# Клас Library: атрибут — список книг (list, за замовчуванням порожній).
# Метод add_book(book): додає об'єкт Book до списку.
# Метод remove_book(title): видаляє книгу за назвою. Виводьте повідомлення, якщо книгу не знайдено.
# Метод find_book(title): шукає і повертає книгу за назвою (часткове співпадіння).
# Метод show_all(): виводить список усіх книг.
print("\n/ООП/ Клас Library — бібліотека")

class Book:
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    # Додаємо зручне відображення книги при виведенні на екран
    def __str__(self):
        return f"'{self.name}' — {self.author}"


class Library:
    def __init__(self):
        # За замовчуванням список книг порожній
        self.books = []

    def add_book(self, book: Book):
        """Додає об'єкт Book до списку."""
        self.books.append(book)
        print(f"Книгу {book} успішно додано!")

    def remove_book(self, title: str):
        """Видаляє книгу за назвою. Виводить повідомлення, якщо не знайдено."""
        for book in self.books:
            if book.name.lower() == title.lower():
                self.books.remove(book)
                print(f"Книгу '{title}' видалено з бібліотеки.")
                return  # Виходимо з методу, бо книгу знайдено і видалено
        print(f"Помилка: Книгу '{title}' не знайдено!")

    def find_book(self, title: str):
        """Шукає і повертає книги за назвою (часткове співпадіння)."""
        found_books = []
        for book in self.books:
            if title.lower() in book.name.lower():  # Часткове співпадіння
                found_books.append(book)

        return found_books

    def show_all(self):
        """Виводить список усіх книг."""
        if not self.books:
            print("Бібліотека порожня.")
        else:
            print("\n--- Список усіх книг у бібліотеці ---")
            for book in self.books:
                print(book)


# --- ПЕРЕВІРКА РОБОТИ КОДУ В PYCHARM ---
# 1. Створюємо бібліотеку
my_library = Library()

# 2. Створюємо кілька книг
book1 = Book("Кобзар", "Тарас Шевченко")
book2 = Book("Гаррі Поттер", "Дж. К. Ролінґ")
book3 = Book("Тигролови", "Іван Багряний")

# 3. Додаємо книги в бібліотеку
my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

# 4. Показуємо всі книги
my_library.show_all()

# 5. Тестуємо пошук (часткове співпадіння)
print("\n--- Результати пошуку за словом 'Поттер' ---")
search_results = my_library.find_book("Поттер")
for b in search_results:
    print(b)

# 6. Видаляємо книгу та перевіряємо знову
print()
my_library.remove_book("Кобзар")
my_library.remove_book("Неіснуюча Книга")  # Перевірка помилки

my_library.show_all()

# 12. Клас Team — спортивна команда
# Клас Player: атрибути — ім'я (str), номер (int), позиція (str).
# Клас Team: атрибути — назва команди (str), список гравців (list).
# Методи Team: add_player(player), remove_player(name), find_player(name), show_roster()
# — аналогічно до Library.
print("\n/ООП/ Клас Team — спортивна команда")

c# 1. Створюємо картку для одного гравця
class Player:
    def __init__(self, name: str, number: int, position: str):
        self.name = name          # Ім'я гравця
        self.number = number      # Номер на футболці
        self.position = position  # Позиція (нападник, воротар тощо)

    # Цей метод  виводить текст, коли ми пишемо print(гравець)
    def __str__(self):
        return f"№{self.number} {self.name} ({self.position})"

# 2. Створюємо команду
class Team:
    def __init__(self, team_name: str):
        self.team_name = team_name  # Назва команди
        self.players = []            # Спочатку список гравців порожній

    # Метод 1: Додати гравця в команду
    def add_player(self, player: Player):
        self.players.append(player)
        print(f"Гравця {player.name} додано до команди {self.team_name}!")

    # Метод 2: Вигнати гравця за ім'ям
    def remove_player(self, name: str):
        for player in self.players:
            if player.name.lower() == name.lower():
                self.players.remove(player)
                print(f"Гравця {name} видалено з команди.")
                return # Успішно видалили, виходимо з функції
        # Якщо цикл закінчився, а return не спрацював — значить гравця не знайшли
        print(f"Помилка: Гравця з ім'ям {name} немає в команді!")

    # Метод 3: Знайти гравця за ім'ям (часткове співпадіння)
    def find_player(self, name: str):
        found = []
        for player in self.players:
            if name.lower() in player.name.lower():
                found.append(player)
        return found

    # Метод 4: Показати весь склад команди
    def show_roster(self):
        if not self.players:
            print(f"Команда {self.team_name} наразі порожня.")
        else:
            print(f"\n--- Склад команди {self.team_name} ---")
            for player in self.players:
                print(player) # Тут спрацює наш __str__ з класу Player


# --- ПЕРЕВІРКА В PYCHARM (Запусти цей код!) ---

# Крок А: Створюємо саму команду
my_team = Team("Шахтар")

# Крок Б: Створюємо окремих гравців (картки)
p1 = Player("Андрій", 7, "Нападник")
p2 = Player("Микола", 10, "Півзахисник")
p3 = Player("Тарас", 4, "Захисник")

# Крок В: Додаємо їх у команду
my_team.add_player(p1)
my_team.add_player(p2)
my_team.add_player(p3)

# Крок Г: Дивимося, хто в команді
my_team.show_roster()

# Крок Ґ: Пробуємо когось видалити
print()
my_team.remove_player("Микола")
my_team.remove_player("Олександр") # Такого немає, виведе помилку

# Крок Д: Фінальний склад
my_team.show_roster()

# 13. Клас Classroom — клас учнів
# Клас Student: атрибути — ім'я (str), оцінка (float).
# Клас Classroom: список учнів.
# Методи: add_student(), remove_student(name), find_student(name), show_all().
# Метод average_grade(): обчислює і повертає середню оцінку по всьому класу.
print("\n/ООП/ Клас Classroom — клас учнів")

# 1. Форма (картка) для одного учня
class Student:
    def __init__(self, name: str, grade: float):
        self.name = name  # Ім'я учня
        self.grade = grade  # Його оцінка

    def __str__(self):
        return f"Учень: {self.name}, Оцінка: {self.grade}"


# 2. Форма для шкільного класу (наша "коробка" з учнями)
class Classroom:
    def __init__(self):
        self.students = []  # Порожній список учнів на початку

    # Метод 1: Додати учня до класу
    def add_student(self, student: Student):
        self.students.append(student)
        print(f"Учня {student.name} додано до класу!")

    # Метод 2: Видалити учня за ім'ям
    def remove_student(self, name: str):
        for student in self.students:
            if student.name.lower() == name.lower():
                self.students.remove(student)
                print(f"Учня '{name}' видалено з класу.")
                return
        print(f"Помилка: Учня з ім'ям '{name}' не знайдено.")

    # Метод 3: Знайти учня за ім'ям (часткове співпадіння)
    def find_student(self, name: str):
        found = []
        for student in self.students:
            if name.lower() in student.name.lower():
                found.append(student)
        return found

    # Метод 4: Показати всіх учнів у класі
    def show_all(self):
        if not self.students:
            print("У класі немає жодного учня.")
        else:
            print("\n--- Список учнів класу ---")
            for student in self.students:
                print(student)

    # Метод 5: Обчислити середню оцінку по всьому класу
    def average_grade(self):
        if not self.students:
            return 0.0  # Якщо учнів немає, середня оцінка нуль

        total_sum = 0
        for student in self.students:
            total_sum += student.grade  # Додаємо оцінку кожного учня

        # Ділимо загальну суму оцінок на кількість учнів
        return total_sum / len(self.students)


# --- ПЕРЕВІРКА РОБОТИ КОДУ В PYCHARM ---

# Створюємо клас
my_classroom = Classroom()

# Створюємо картки учнів
s1 = Student("Марія", 11.5)
s2 = Student("Іван", 9.0)
s3 = Student("Олена", 10.2)

# Додаємо учнів у клас
my_classroom.add_student(s1)
my_classroom.add_student(s2)
my_classroom.add_student(s3)

# Показуємо весь клас
my_classroom.show_all()

# Рахуємо та виводимо середній бал
avg = my_classroom.average_grade()
print(f"\nСередня оцінка класу: {avg:.2f}")

# Тестуємо видалення
print()
my_classroom.remove_student("Іван")

# Дивимося оновлений середній бал
new_avg = my_classroom.average_grade()
print(f"Нова середня оцінка класу: {new_avg:.2f}")


    # --- Рівень 4. СИСТЕМИ З ДВОХ КЛАСІВ ---
# 14. Інтернет-магазин
# Клас Product: атрибути — назва (str), ціна (float).
# Клас Cart (кошик): список товарів.
# Метод add_item(product): додає товар до кошика.
# Метод remove_item(name): видаляє товар за назвою.
# Метод total(): обчислює і повертає загальну суму всіх товарів у кошику.
# Метод display(): виводить вміст кошика і загальну суму.

# 15. Телефонна книга
# Клас Contact: атрибути — ім'я (str), номер телефону (str).
# Клас PhoneBook: список контактів.
# Методи: add_contact(contact), remove_contact(name), find_contact(name) — пошук за
# частиною імені, show_all() — всі контакти за алфавітом.

# 16. Плейлист
# Клас Song: атрибути — назва (str), виконавець (str).
# Клас Playlist: назва плейлиста (str), список пісень.
# Методи: add_song(song), remove_song(title), find_song(title), show() — виводить усі пісні
# з нумерацією.



# --- Рівень 5. МЕНЮ ТА ТЕКСТОВИЙ ІНТЕРФЕЙС ---
# 17. Менеджер завдань
# Клас Task: атрибути — назва (str), опис (str), статус (str): "нове" або "виконано".
# Клас TaskManager: список завдань.
# Методи: add_task(), remove_task(name), complete_task(name) — змінює статус на
# "виконано", show_all().
# Текстове меню (while True): 1 — Додати завдання (ввести назву і опис). 2 —
# Видалити завдання. 3 — Позначити як виконане. 4 — Показати всі завдання. 0 — Вийти.

# 18. Бібліотечна система
# Клас Book: атрибути — назва (str), автор (str), is_available (bool, за замовчуванням True).
# Клас Library: список книг.
# Метод issue_book(title): позначає книгу як видану (is_available = False). Перевіряйте  доступність.
# Метод return_book(title): повертає книгу (is_available = True).
# Текстове меню: 1 — Додати книгу. 2 — Видати книгу. 3 — Повернути книгу. 4 —
# Показати всі книги (з позначкою доступності). 5 — Пошук книги. 0 — Вийти.

# 19. Симулятор банкомату
# Клас Account: атрибути — власник (str), PIN (str), баланс (float).
# Клас ATM: список рахунків (dict або list).
# Метод find_account(owner): знаходить рахунок за ім'ям власника.
# Текстове меню: 1 — Створити рахунок (ввести ім'я, PIN, початковий баланс). 2 —
# Поповнити рахунок (ввести ім'я, PIN, суму). 3 — Зняти гроші (перевіряти PIN і наявність
# коштів). 4 — Показати баланс (після перевірки PIN). 0 — Вийти.
