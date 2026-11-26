##########################################
# Here is the skeleton of the Dockerfile #
##########################################
# FROM base image
# COPY the `uv` binary
# COPY dependencies (2 files!)
# RUN install dependencies
# COPY the code
# CMD launch the API web server

FROM python:3.12-trixie

#COPY
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY src src
COPY api api
COPY models models
COPY pyproject.toml pyproject.toml
COPY uv.lock uv.lock
COPY README.md README.md

#ENV
ENV UV_NO_DEV=1 \
    UV_FROZEN=1

#RUN
RUN uv sync

#CMD ,"--port", "8080"
CMD ["uv", "run", "uvicorn", "api.fast:app", "--host", "0.0.0.0"]
