#!/bin/bash
echo "WARNING: Run this script only from the ~/RowingClubWebsite/Website directory."
sudo rm -f /etc/nginx/sites-enabled/website
sudo rm -f /etc/nginx/sites-available/website
sudo rm -f /etc/nginx/nginx.conf
sudo systemctl stop nginx
sudo systemctl disable nginx
$(sudo fuser -fk 80/tcp) | echo
