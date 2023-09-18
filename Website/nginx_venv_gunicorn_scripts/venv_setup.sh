#!/bin/bash
echo "WARNING: Run this script only from the website root directory."
rm -rf website_venv
rm -f wsgi.py
python3 -m venv website_venv
source website_venv/bin/activate
pip install gunicorn flask flask_login flask_mail python-dateutil
cp nginx_venv_gunicorn_scripts/wsgi.py . 
