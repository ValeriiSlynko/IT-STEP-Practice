import time
from settings import settings

while True:
    time.sleep(2)
    print(f"\nName app: {settings.app_name}")
    print(f"File name: {settings.filename}")
    print(f"Login app: {settings.login}")
    print(f"Password app: {settings.password}")
