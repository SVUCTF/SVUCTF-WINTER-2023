#!/usr/bin/env sh

gunicorn app:app -b 0.0.0.0:5000 -D
python bot/bot.py