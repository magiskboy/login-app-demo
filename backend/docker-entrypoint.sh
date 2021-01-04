#!/bin/sh

gunicorn -c gunicorn.py wsgi:app
