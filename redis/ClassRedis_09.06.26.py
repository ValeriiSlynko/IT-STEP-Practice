# redis в python
from redis import Redis

# підключення
host = "localhost"
port = 6379

server = Redis(
        host="localhost",
        port=6379,
        db=0,     # індекс бази даних
        decode_responses=True   # щоб повертало не сирі байти
)

# отримати значення ключа
user_name = server.get("name")
print(user_name)
print(type(user_name))

# добавити новий ключ
server.set("name", "Valery")

# Модуль 16
# Використання баз даних (частина 3)
# Взаємодія з Redis через консоль

# Завдання 1 Запуск сервера Redis
# Встановіть Redis на свій комп'ютер.
# Запустіть сервер Redis через консоль.

# Завдання 2
# Додавання ключа-значення Використовуючи команду SET, додайте ключ "name" і значення "John Doe".
user_name = server.set(name="name", value="Valery")
print(user_name)

# Завдання 3
# Отримання значення за ключем за допомогою команди GET, отримайте значення ключа "name".
name = server.get("name")
print(name)

# Завдання 4 Додавання списку
#  Використовуючи команду RPUSH, додайте до списку "fruits" елементи "apple", "banana", "orange".
server.rpush("fruits" "apple" "banana" "orange")
print(server.get("fruits"))

# Завдання 5 Отримання елементів списку
#  За допомогою команди LRANGE, отримайте всі елементи зі списку "fruits".
fruits=server.lrange("fruits", 0, -1)
print(fruits)

# Завдання 6 Додавання хешу
# Використовуючи команду HMSET, додайте до хешу "user:1" поля "name" зі значенням "Alice" і "age" зі значенням 25.
data = {
        "name": "Alice",
        "age": 25,
}
server.hmset("user:1", data)

# Завдання 7
# Отримання значень з хешу за допомогою команди HGETALL, отримайте всі поля та значення з хешу "user:1".
server.hgetall("user:1")

# Завдання 8
# Додавання елементу до множини використовуючи команду SADD, додайте до множини "tags" елементи "red", "green", "blue".
server.sadd("tags", "red", "green", "blue")

# Завдання 9
# Отримання всіх елементів множини за допомогою команди SMEMBERS, отримайте всі елементи з множини "tags".
name = server.smembers("tags")

# Завдання 10
# Додавання лічильника використовуючи команду INCR, додайте до лічильника "counter" одиницю.
server.incr("counter", 20)
print(name)

# Завдання 11
# Отримання значення лічильника за допомогою команди GET, отримайте значення лічильника "counter".
total = server.zcard("counter")
print(total)

# Завдання 12
# Видалення ключа використовуючи команду DEL, видаліть ключ "name".
server.delete("name")

# Завдання 13
# Перевірка існування ключа за допомогою команди EXISTS, перевірте існування ключа "name".
is_exists = server.exists("name")
is_exists = bool(is_exists)
print(is_exists)

# Завдання 14
# Додавання значення з таймаутом використовуючи команду SETEX, додайте ключ "message"
# зі значенням "Hello, Redis!" і таймаутом 60 секунд.
server.setex("message", 60, "Hello, Redis!")
text = server.get("message")
print(text)

# Завдання 15
# Очищення всіх ключів використовуючи команду FLUSHALL, очистіть всі ключі та дані в Redis.
server.flushall()

# Завдання 16
# Геоаналітика з Redis створіть ключ "geo_locations" та додайте до нього геодані
# (координати) різних місць в вашому місті. Використовуйте команду GEOADD для додавання геоданих.
server.geoadd("geo_locations",
        (36.2328, 49.9883, "Kharkiv_Center", 36.2336, 49.9923, "Pushkinska_St", 36.2312, 50.0006, "Sumska_St"))
print("Геодані Харкова успішно додано!")

# Завдання 17 Хешування
#  Створіть у Redis ключ "students" і додайте до нього
# інформацію про студентів у вигляді хешу, де ключ - ім'я студента, а значення - його середній бал.
# Виведіть інформацію про всіх студентів, змініть середній бал одного із студентів та виведіть оновлену інформацію.
server.hset("students", mapping={"Valery": 9 , "Viktor": 10 , "Ivan": 12})

# завдання 17.1 Виводимо інформацію про всіх студентів
all_students = server.hgetall("students")
print("Всі студенти:", all_students)

# завдання 17.2 Змінюємо середній бал одного із студентів
server.hset("students", "Valery", 11)

# Завдання 17.3 Виводимо оновлену інформацію про студентів
updated_students_info = server.hgetall("students")
print("Оновлені дані про студентів", updated_students_info)

# Завдання 18
# Статистика унікальних користувачів
# Створіть гіперлоглог "unique_users" та додайте до нього ідентифікатори унікальних користувачів
# за допомогою команди PFADD.
server.pfadd("unique_users", "user_id_1" "user_id_2" "user_id_3")
unique_users = server.pfcount("unique_users")
print("Кількість унікальних користувачів:", unique_users)

# Завдання 19 Використання транзакцій
# Використовуючи команду MULTI, розпочніть транзакцію.
# Додайте декілька команд до транзакції, наприклад, додавання до списку та хешу.
# Використовуючи команду EXEC, виконайте транзакцію.
pipe = server.pipeline()

# Додаємо команди в транзакцію
pipe.rpush("actions", "login")
pipe.hset("session:1", "status", "active")

# Використовуючи команду EXEC, виконайте транзакцію
transaction_result = pipe.execute()
print("Результат транзакції:", transaction_result)

# Завдання 20 Закриття сервера Redis
# Закрийте сервер Redis через консоль.
