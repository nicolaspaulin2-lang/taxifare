FROM python:3.12-trixie

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY api api
COPY src src
COPY pyproject.toml pyproject.toml
COPY uv.lock uv.lock
COPY README.md README.md
COPY models models

RUN uv sync
#  "--port"

CMD ["uv", "run", "uvicorn", "api.fast:app", "--host", "0.0.0.0"]
