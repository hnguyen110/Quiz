FROM python:3 as build
ENV PIPENV_VENV_IN_PROJECT=1
WORKDIR /app
RUN apt-get update \
  && apt-get install python3-dev default-libmysqlclient-dev gcc -y
RUN pip install --upgrade pip
RUN pip install pipenv
COPY Pipfile Pipfile.lock /app/
RUN pipenv install
COPY . .

FROM python:alpine3.16 as production
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY --from=build /app /app
EXPOSE 80
CMD .venv/bin/gunicorn quiz.wsgi -w 10 -b 0.0.0.0:80