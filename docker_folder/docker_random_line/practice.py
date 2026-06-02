# Створіть файл practice.py
# Напишіть код який раз в delay секунди виводить рядки з
# символів symbol довжиною від min_len до
# max_len(вибрати довжину випадково)
# Приклад для значень за замовчуванням
# --------
# ----------
# -------
# ---------
# -------
# Запустіть файл practice через Pycharm

import time
import random

from settings import settings

while True:
    time.sleep(settings.delay)

    random_len = random.randint(settings.min_len, settings.max_len)
    print(settings.symbol * random_len)
