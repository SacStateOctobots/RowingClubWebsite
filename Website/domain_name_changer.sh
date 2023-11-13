#!/bin/bash

# Read in the domain name from the user
read -p "Enter the new domain name: " domain

# Write out the new config for the https key script
echo "Rewriting ./nginx_venv_gunicorn_scripts/gen_ca_https_key.sh to use" $domain
#!/bin/bash
#sudo certbot --nginx -d octobotgroup.work
echo "#!/bin/bash" > ./nginx_venv_gunicorn_scripts/gen_ca_https_key.sh
echo "sudo certbot --nginx -d" $domain >> ./nginx_venv_gunicorn_scripts/gen_ca_https_key.sh
chmod +x ./nginx_venv_gunicorn_scripts/gen_ca_https_key.sh

# Write out the new config for nginx
echo "Rewriting ./nginx_venv_gunicorn_scripts/website to use" $domain
echo -e "server {" > ./nginx_venv_gunicorn_scripts/website
echo -e "\tlisten 80;" >> ./nginx_venv_gunicorn_scripts/website
echo -e "\tserver_name" $domain";" >> ./nginx_venv_gunicorn_scripts/website
echo -e "" >> ./nginx_venv_gunicorn_scripts/website
echo -e "\tlocation / {" >> ./nginx_venv_gunicorn_scripts/website
echo -e "\t\tinclude proxy_params;" >> ./nginx_venv_gunicorn_scripts/website
echo -e "\t\tproxy_pass http://unix:/home/ubuntu/RowingClubWebsite/Website/website.sock;" >> ./nginx_venv_gunicorn_scripts/website
echo -e "\t}" >> ./nginx_venv_gunicorn_scripts/website
echo -e "}" >> ./nginx_venv_gunicorn_scripts/website

