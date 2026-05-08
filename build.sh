#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
npm ci
npm run css:build
python manage.py collectstatic --no-input
python manage.py migrate
if [ -f data.xlsx ]; then
  python manage.py import_participants data.xlsx
fi
