

FROM python:3.14-slim

WORKDIR app

COPY ./ ./

# встановлення бібліотек
RUN pip install -r requirements.txt

# відкрити порт
EXPOSE 8080

CMD ["python3", "practice.py"]
