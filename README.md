# fast-api-base

## Setup

Build project:
- Install [docker](https://docs.docker.com/engine/install/) and [docker-compose](https://docs.docker.com/compose/install/).

Try next commands with `sudo` if you get permission errors.
- `docker-compose build`.
- `docker-compose up -d`.
- Server will run in port 8000.


- To run without docker: `uvicorn src.main:app --reload`

### Requirements

This projects requires python 3.10.
Python 3 can be installed with [pyenv](https://github.com/pyenv/pyenv).

1. Use [pyenv-installer](https://github.com/pyenv/pyenv-installer) for installing pyenv
1. See which python versions are available: `pyenv install --list`
1. Install python 3. Example: `pyenv install 3.10.5` (3.10.0 or higher)
1. `pyenv shell 3.10.5`
1. `poetry shell`


## Install new dependencies
This project uses [poetry](https://python-poetry.org/). as a dependency manager.
- `poetry shell`.
- `poetry add {dependency_name}`.

## Errors along the way
1. Poetry doesn't seem to install correctly with `pyenv`, install python using `brew` in Mac.