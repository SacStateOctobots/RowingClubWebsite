#!/bin/bash
echo "WARNING: Run this script only from the website root directory."
rm -rf website_venv
rm -f wsgi.py
python3 -m venv website_venv
source website_venv/bin/activate
pip install gunicorn flask==2.2.2 werkzeug==2.2.2 flask_login==0.6.2 flask_mail==0.9.1 python-dateutil
cp nginx_venv_gunicorn_scripts/wsgi.py . 
