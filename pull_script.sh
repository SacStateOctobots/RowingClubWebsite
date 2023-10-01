#!/bin/bash

# check that script is ran from the correct directory
if [ $(pwd) != $HOME ]; then
	echo "Please run this script only from your home directory: $HOME"
	exit
fi

# check if pull directory already exists, if so delete it
if [ -d "./pullDirectory" ]; then
	echo "./pullDirectory already exists, deleting old directory."
	rm -rf ./pullDirectory
	echo "Deletion complete."
fi

# pull code from our repo to pullDirectory
mkdir -p pullDirectory
cd pullDirectory
git clone https://github.com/SacStateOctobots/RowingClubWebsite.git

# give execute permissions to all scripts in nginx_script directory
echo "Adding execute permissions for deploy script:"
for str in $(ls RowingClubWebsite/Website/nginx_venv_gunicorn_scripts/ | egrep '*.sh'); do
	echo RowingClubWebsite/Website/nginx_venv_gunicorn_scripts/$str
	chmod +x RowingClubWebsite/Website/nginx_venv_gunicorn_scripts/$str
done

# move back up to home directory
echo "Backing up old site deployment"
cd ~
mv RowingClubWebsite RowingClubWebsite_$(date +"%Y-%m-%d-%T").backup
mv pullDirectory/RowingClubWebsite/ RowingClubWebsite
rm -rf pullDirectory

# key and email address files still need to be copied over
echo "Site is downloaded. You must now copy the API_KEY, EMAIL_ADDRESS and EMAIL_KEY files to /home/ubuntu/RowingClubWebsite/Website before running make deploy."
