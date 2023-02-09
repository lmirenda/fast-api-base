#!/bin/bash

# Let the db start
python backend_pre_start.py

# Run migrations
alembic upgrade head
