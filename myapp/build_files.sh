#!/bin/bash
echo " BUILD START "
# Install dependencies
python3.12 -m pip install -r requirements.txt

# Create the database tables
python3.12 manage.py makemigrations --noinput
python3.12 manage.py migrate --noinput

# Collect static files
python3.12 manage.py collectstatic --noinput --clear
echo " BUILD END "