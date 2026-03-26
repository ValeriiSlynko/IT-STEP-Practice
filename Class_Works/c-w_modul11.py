# Курс: AI+Python
# Модуль 11. ООП
# Тема: ООП. Частина 1

# Завдання 1
# Створіть клас Student з атрибутами name та age. Додайте
# метод для виводу інформації у форматі «Ім’я: {name}, вік: {age}»



# Завдання 2
# Створіть список з 3-ма студентами, дані вводить користувач.
# Після чого для кожного студента виведіть інформацію про нього за допомогою метода.

class Student():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def student_info (self):
        print(f"Ім'я: {self.name}, Вік: {self.age}")

student_1 = Student (name= "Валерій", age = 37 )
student_2 = Student (name= "Глєб", age = 38 )
student_3 = Student (name= "Джек", age = 39 )

students = []

students.append(student_1)
students.append(student_2)
students.append(student_3)

print(students)


# Завдання 3
# Створіть клас Circle з атрибутом radius.
# Додайте метод для отримання площі кола

import math

class circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * math.pi * self.radius





# Завдання 4
# Створіть клас BankAccount з атрибутами owner та balance.
# Додайте метод deposit для поповнення рахунку
# Додайте метод withdraw для зняття грошей з рахунку
# Додайте метод info для виведення інформації про баланс



# Завдання 5
# Створіть клас Car з атрибутами brand(марка), year(рік
# випуску), is_ready(чи готовий до поїздки, за замовчування False).
# Додайте метод start_engine який заводить двигун, і змінює атрибут is_ready
# Додайте метод move який виводить повідомлення, що
# автомобіль їде, або ж ще не готовий в залежності від is_ready.
