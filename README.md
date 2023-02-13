# fast-api-base

## Setup

Build project:
- Install [docker](https://docs.docker.com/engine/install/) and [docker-compose](https://docs.docker.com/compose/install/).

Try next commands with `sudo` if you get permission errors.
- `docker-compose build`.
- `docker-compose up -d`.
- Server will run in port 8080.


- To run without docker: `uvicorn src.main:app --reload`

### Requirements

This projects requires python 3.11.0
Python 3 can be installed with [pyenv](https://github.com/pyenv/pyenv).

1. Use [pyenv-installer](https://github.com/pyenv/pyenv-installer) for installing pyenv
2. See which python versions are available: `pyenv install --list`
3. Install python 3. Example: `pyenv install 3.11.0` (3.11.0 or higher)
4. `pyenv shell 3.11.0`
5. `poetry shell`

> If `poetry shell` is not working, try running:
> `poetry env use python3.11`.
> 
> Then, restart your shell for the changes to take effect.

## Install new dependencies
This project uses [poetry](https://python-poetry.org/). as a dependency manager.
- `poetry shell`.
- `poetry add {dependency_name}`.

## Testings the application
- All tests are run using the `pytest` command in the CLI. 