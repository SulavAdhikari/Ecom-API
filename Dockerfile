FROM python:3.11.1


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app


ENV DJANGO_SETTINGS_MODULE=ecom.settings

RUN pip install -r requirements.txt

CMD ["sh","python","manage.py","makemigrations","&&","python","manage.py","migrate","--run-syncdb","&&","python", "manage.py", "runserver"]