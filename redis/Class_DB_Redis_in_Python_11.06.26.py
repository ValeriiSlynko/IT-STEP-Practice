# Курс: «Введення в мову
# програмування Python
# Модуль 16. Використання баз даних
# Тема: Використання баз даних. Частина 5
# Завдання 1
# Створіть додаток «Соціальна мережа», який зберігає
# інформацію про користувача, його друзів, публікації користувача. Можливості додатку:
# ■ вхід за логіном і паролем;
# ■ додати користувача;
# ■ видалити користувача;
# ■ редагувати інформацію про користувача;
# ■ пошук користувача за ПІБ;
# ■ перегляд інформації про користувача;
# ■ перегляд усіх друзів користувача;
# ■ перегляд усіх публікацій користувача.
# Зберігайте дані у базі даних NoSQL. Можете використовувати Redis в якості платформи.

#  ??? - // - // - // - // - // - ???


# Завдання 2
# Створіть додаток «Музей літератури». Додаток має зберігати
# інформацію про експонати та людей, які мають відношення
# до експонатів. Можливості додатку:
# ■ вхід за логіном і паролем;
# ■ додати експонат;
# ■ видалити експонат;
# ■ редагування інформації про експонат;
# ■ перегляд повної інформації про експонат;
# ■ виведення інформації про всі експонати;
# ■ перегляд інформації про людей, які мають відношення до певного експонату;
# ■ перегляд інформації про експонати, що мають відношення до певної людини;
# ■ перегляд набору експонатів на основі певного критерію.
# Наприклад, показати всі книжкові експонати.
# Зберігайте дані у базі даних NoSQL. Можете використовувати Redis в якості платформи.

from redis import Redis

# ■ вхід за логіном і паролем;
class LiteratureMuseum():
    def __init__(self):
        self.server = Redis(
            host='localhost',
            port=6379,
            db=0,
            decode_responses=True
        )

        self.current_user = None
        self.isloggedin = False

    def _get_cred_key(self, user_name):
        return f"password:{user_name}"

    def _get_exponat_key(self,exp_name):
        return f"exponent:{exp_name}"

    def _get_people_key(self, person_name):
        return f"people:{person_name}"

    def _get_exp_related_name_key(self,exp_name):
        return f"exponat{exp_name}:people"

    def login(self, user_name, password):
        key = self._get_cred_key(user_name)

        if not self.server.exists(key):
            print("user already exists")
            return

        true_password = self.server.get(key)

        if true_password != password:
            print("wrong password")
            return

        print("you are logged in")
        self.isloggedin = True

    def signup(self, user_name, password):
        key = self._get_cred_key(user_name)

        if self.server.exists(key):
            print("user already exists")
            return

        self.server.set(key, password)

        print("you are registered now")

    def add_exp_info(self,exp_name, desc):
        key = self._get_exponat_key(exp_name)

        if not self.isloggedin:
            print("not logged in")
            return

        self.server.set(key, desc)
        print("exp info added")

# save password:valery 12345
# save exponat:name description
# save people:name description
# save exponat:name:people: name

app = LiteratureMuseum()

app.login("valery_slynko", "5456")

app.add_exp_info("triangle", "figure1")
app.add_exp_info("rectangle", "figure2")
