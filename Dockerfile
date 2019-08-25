FROM kennethreitz/pipenv as build

COPY . /app

VOLUME "/app/data/redis"

CMD python3 /app/main.py

