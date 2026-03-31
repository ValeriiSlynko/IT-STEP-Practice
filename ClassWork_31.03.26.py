# Курс: AI+Python
# Модуль 11. ООП
# Тема: ООП. Частина 1

#   ЗАВДАННЯ 1
# Створіть клас Проект з атрибутами:
#  назва
#  виділений кошторис
#  загальні витрати
#  чи завершений(за замовчуванням False)
#  час виконання(за замовчуванням 0 місяців)
#  список необхідних задач
# Додайте методи:
#  вивід інформації: назва, час виконання, необхідні задачі
#  добавити нову задачу
#  розбити задачу на під-задачі: передається назва задачі та список під-задач
#  виконати задачу, передається назва, час та ціна виконання
#  поповнення кошторису
from typing import List


class Project:
    def __init__(self, name: str, budget: int) -> None:
        self.name = name
        self.budget = budget

        self.expenses = 0
        self.is_finished = False
        self.time_of_processed = 0
        self.tasks: List[str] = []

    # Вивід інформації
    def show_info(self):
        print(f"\nПроект: {self.name}")
        print(f"Час виконання: {self.time_of_processed} годин")

        if not self.tasks:
            print("Немає задач")
        else:
            print("Етапи виробництва:")
            for task in self.tasks:
                print(f"- {task}")

    # Додати етап
    def add_task(self, task_name: str):
        self.tasks.append(task_name)

    # Додати підетапи (просто текстом)
    def split_task(self, task_name: str, subtasks: List[str]):
        for i in range(len(self.tasks)):
            if self.tasks[i] == task_name:
                self.tasks[i] = task_name + " (" + ", ".join(subtasks) + ")"

    # Завершити етап
    def complete_task(self, task_name: str, time: int, cost: int):
        if task_name in self.tasks:
            self.time_of_processed += time
            self.expenses += cost

    # Поповнення бюджету
    def add_budget(self, amount: int):
        self.budget += amount

project = Project("Виробництво автомобіля", 50000)

project.add_task("Двигун")
project.add_task("Кузов")
project.add_task("Збірка")

project.split_task("Двигун", ["деталі", "збірка"])
project.split_task("Кузов", ["штамповка", "фарбування"])

project.complete_task("Двигун", 10, 15000)
project.complete_task("Кузов", 8, 12000)

project.show_info()

#   ЗАВДАННЯ 2
# Створіть клас Телефон з атрибутами:
#  максимальний обсяг пам’яті
#  зайнята пам’ять
#  чи включений(за замовчуванням False)
#  встановлені додатки у вигляді словника, де ключ – назва додатку, значення – обсяг пам’яті
# Додайте методи:
#  вивести інформацію про використання пам’яті
#  видалити додаток
#  встановити новий додаток, якщо пам’яті достатньо
#  оновити додаток(нова версія може займати іншу кількість пам’яті)
#  запустити додаток, якщо він є і якщо телефон включений
#  включити телефон
#  виключити телефон
from typing import  Dict

class Phone:

    def __init__(self, max_memory: int):
        self.max_memory = max_memory
        self.used_memory: int = 0
        self.is_on: bool = False
        self.apps: Dict[str,int] = {}

    def show_info(self):
        status = "Ввімкнено" if self.is_on else "Вимкнено"
        print("--- Інформація про телефон ---")
        print(f"Статус: {status}")
        print(f"Пам'ять: {self.used_memory} / {self.max_memory} МБ")

        if self.apps:
            print("Встановлені додатки:")
            for name, size in self.apps.items():
                print(f" - {name}: {size} МБ")
        else:
            print("Встановлених додатків немає.")
        print("------------------------------")

    def install_app(self, app: str, size: int):
        if self.used_memory + size > self.max_memory:
            print("Недостатньо пам'яті")
            return

        self.apps[app] = size
        self.used_memory += size

    def delete_app(self, app: str):
        if app in self.apps:
            size = self.apps.pop(app)
            self.used_memory -= size

phone1 = Phone(126)
phone1.show_info()
phone1.install_app("Telegram", 20)
phone1.install_app("Google", 10)

phone1.show_info()
phone1.delete_app("TG")
phone1.show_info()

# Завдання 3
# Створіть клас Автомобіль з атрибутами:
#  марка
#  пробіг
#  рівень пального
#  витрата пального(л/км)
#  чи є справним(за замовчуванням True)
# Реалізуйте методи:
#  проїхати певну відстань, має змінитись пробіг та рівень
# пального, якщо автомобіль справний та достатньо
# пального
# З ймовірністю 40% автомобіль може зламатись
#  ремонт
#  поповнення пального
# Завдання 4
# Створіть клас Студент з атрибутами:
#  ім’я
#  словник з предметами, де ключ – назва предмету,
# значення – список оцінок
# Додайте методи:
#  додати новий предмет
#  видалити предмет
#  вчити предмет(якщо отримана оцінка, то додати про це
# інформацію)
#  отримати середню оцінку за конкретним предметом
#  вивести загальну інформацію: ім’я та список предметів
# з середніми оцінками
# Завдання 5
# Створіть клас Магазин з атрибутами:
#  назва
#  заробіток
#  словник з товарами, де ключ – назва товару, значення –
# кількість на складі
#  словник з товарами, де ключ – назва товару, значення –
# ціна
# Додайте методи:
#  вивід інформації: назва та список доступних товарів
#  поповнення складу певним товаром(може бути новий)
#  оформлення замовлення, якщо товар у достатній
# кількості доступний
