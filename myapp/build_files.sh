#!/bin/bash
echo "BUILD START"
python3.12 -m pip install -r requirements.txt

# Run migrations to create the tables in the database
python3.12 manage.py migrate --noinput
python3.12 manage.py collectstatic --noinput --clear
echo "BUILD END"