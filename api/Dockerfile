FROM python:3.7

LABEL Author="Brylie Christopher Oxley"
LABEL E-mail="brylie.oxley@maas.global"
LABEL version="0.0.1"

LABEL Name=sustainable-mobility-api Version=0.0.1
EXPOSE 8080

RUN mkdir --parents /app
WORKDIR /app
COPY . /app

RUN python -m pip install pipenv
RUN pipenv install --ignore-pipfile
CMD ["pipenv", "run", "python3", "-m", "api"]
