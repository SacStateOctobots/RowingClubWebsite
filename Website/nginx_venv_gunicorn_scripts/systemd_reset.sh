#!/bin/bash
echo "WARNING: Run this script only from the ~/RowingClubWebsite/Website directory."
sudo systemctl stop website
sudo systemctl disable website
sudo systemctl status website
sudo rm -f /etc/systemd/system/website.service
sudo rm -f wsgi.py
