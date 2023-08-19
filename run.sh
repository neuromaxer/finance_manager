#!/bin/bash

# Start Django server
cd finance_manager
pipenv run python manage.py runserver &

# Start React frontend
cd ../frontend
npm start &

# Wait for all child processes to finish
wait
