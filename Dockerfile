FROM kennethreitz/pipenv as build

COPY . /app

VOLUME "/app/data/redis"

EXPOSE 9090

CMD python3 /app/app.py

