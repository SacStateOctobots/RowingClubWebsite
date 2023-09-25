#!/bin/bash
echo "WARNING: Run this script only from the ~/RowingClubWebsite/Website directory."
# delete old configs
sudo rm -f /etc/nginx/sites-enabled/website
sudo rm -f /etc/nginx/sites-available/website
sudo rm -f /etc/nginx/nginx.conf
# copy over new configs
sudo cp nginx_venv_gunicorn_scripts/nginx.conf /etc/nginx/
sudo cp nginx_venv_gunicorn_scripts/website /etc/nginx/sites-available/website
sudo ln -s /etc/nginx/sites-available/website /etc/nginx/sites-enabled

# startup nginx systemd service
sudo systemctl start nginx
sudo systemctl enable nginx
sudo systemctl status nginx
sudo systemctl daemon-reload
