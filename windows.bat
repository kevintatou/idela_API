@echo off
ssh -f -N -L 4321:127.0.0.1:27017 root@207.154.211.98
python manage.py runserver