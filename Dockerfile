# Указывает Docker использовать официальный образ python 3 с dockerhub в качестве базового образа
FROM python:3.11.8-bookworm
# Устанавливает переменную окружения, которая гарантирует, что вывод из python будет отправлен прямо в терминал без предварительной буферизации
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
# Устанавливает рабочий каталог контейнера — "app"
WORKDIR /usr/src/shorturl
# Копирует все файлы из нашего локального проекта в контейнер
COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt
# Запускает команду pip install для всех библиотек, перечисленных в requirements.txt
COPY . /usr/src/shorturl/

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]