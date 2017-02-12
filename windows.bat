@echo off
ssh -f -N -L 4321:127.0.0.1:27017 88.131.100.92
python manage.py runserver