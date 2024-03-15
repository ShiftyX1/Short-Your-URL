
FROM python:3.11.8-bookworm

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /usr/src/shorturl

COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt

COPY . /usr/src/shorturl/

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]