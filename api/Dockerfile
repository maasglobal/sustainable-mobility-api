FROM python:3.8-slim

LABEL Author="Brylie Christopher Oxley"
LABEL E-mail="brylie.oxley@maas.global"
LABEL version="1.0.0"

LABEL Name=sustainable-mobility-api Version=1.0.0
EXPOSE 8080

RUN mkdir --parents /app
WORKDIR /app
COPY . /app

RUN pip install pipenv
RUN pipenv install --deploy
CMD pipenv run python app.py
