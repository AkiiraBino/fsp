FROM python:3.11

WORKDIR /app

RUN pip install poetry

COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false && poetry install

COPY . /app
COPY ./docker_files/wait-for-command.sh /wait-for-command.sh
COPY ./docker_files/entrypoint.sh /docker-entrypoint.sh

RUN chmod +x "/docker-entrypoint.sh"

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD alembic upgrade head && uvicorn src.main:app --reload --host 0.0.0.0 --port 8080