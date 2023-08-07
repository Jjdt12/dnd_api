#!/bin/sh

export FLASK_APP=./dnd_character_api/index.py

pipenv run flask --debug run -h 0.0.0.0
