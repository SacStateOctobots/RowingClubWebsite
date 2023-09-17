#!/bin/bash
echo "WARNING: Run this script only from the ~/RowingClubWebsite/Website directory."
# release port gunicorn runs on
sudo fuser -k 8000/tcp
sudo rm -f /etc/systemd/system/website.service
sudo rm -f wsgi.py
sudo cp nginx_venv_gunicorn_scripts/website.service /etc/systemd/system/website.service
sudo cp nginx_venv_gunicorn_scripts/wsgi.py .
sudo systemctl start website
sudo systemctl enable website
sudo systemctl status website
sudo systemctl daemon-reload
