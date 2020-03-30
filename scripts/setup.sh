#!/bin/bash
set -e
db_name = "highly_composite"
password=$(openssl rand -hex 32)
scripts/createdb.sh "${db_name}" "${password}"
echo "DATABASE_URL=postgres://${db_name}_user:$password@localhost:5432/$db_name" >> .env
key=$(openssl rand -base64 16)
echo "DJANGO_SECRET_KEY=\"$key\"" >> .env
