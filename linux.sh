#!/bin/bash
python3 manage.py runserver 0.0.0.0:8000 &
autossh -f -N -L 4321:127.0.0.1:27017 88.131.100.92
