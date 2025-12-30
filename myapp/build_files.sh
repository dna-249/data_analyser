#!/bin/bash
echo "BUILD START"
# Use --no-cache to keep the environment slim
python3.12 -m pip install --no-cache-dir -r requirements.txt
python3.12 manage.py collectstatic --noinput --clear
echo "BUILD END"