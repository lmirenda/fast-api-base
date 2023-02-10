FROM python:3.11.0

ARG ENV

ENV TZ=America/Argentina/Buenos_Aires \
    LANG=en_US.UTF-8 \
    LC_ALL=en_US.UTF-8 \
    BASE_DIR=/app/ \
    MEDIA_ROOT=/app/media/ \
    STATIC_ROOT=/app/static/ \
    APP_DIR=/app/code/ \
    POETRY_VERSION=1.3.2

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# System deps:
RUN pip3 install --upgrade pip
RUN pip3 install "poetry==$POETRY_VERSION"

WORKDIR $APP_DIR

# Copy only requirements to cache them in docker layer
COPY poetry.lock pyproject.toml $APP_DIR

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install --no-root

# Creating folders, and files for a project:
COPY . $APP_DIR

EXPOSE 8000
