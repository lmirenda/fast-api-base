#!/bin/sh
echo "Creating default user"
psql -U postgres -c "CREATE ROLE $DEFAULT_DEV_USER WITH PASSWORD '$DEFAULT_DEV_PW' LOGIN SUPERUSER"
psql -U postgres -c "CREATE DATABASE $DEFAULT_DEV_DB_NAME"
psql -U postgres -c "ALTER DATABASE $DEFAULT_DEV_DB_NAME OWNER TO $DEFAULT_DEV_USER"
echo "User created"

psql -U postgres -c 'CREATE DATABASE "fast-api-db"'