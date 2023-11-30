run_local:
	flask --app server run
run_remote:
	gunicorn -w 4 -b 0.0.0.0 'server:app' --keyfile private_key.pem --certfile certificate.pem
setup_db:
	python3 setup_database.py
reset_db:
	python3 delete_db_and_data.py
gen_selfsign_keys:
	# bash syntax doesn't play nicely with make syntax so we can put the command we want to run in here
	nginx_venv_gunicorn_scripts/gen_selfsign_https_key.sh
reset_selfsign_keys:
	sudo rm -f private_key.pem 
	sudo rm -f certificate.pem
deploy:
	# setup database
	python3 setup_database.py
	# set up virtual environment
	nginx_venv_gunicorn_scripts/venv_setup.sh
	# set up systemd gunicorn
	nginx_venv_gunicorn_scripts/systemd_setup.sh
	# set up nginx 
	nginx_venv_gunicorn_scripts/nginx_setup.sh
	# set up keys
	echo "NOTE: If option 2 for the key setup fails due to rate limiting, try option 1."
	nginx_venv_gunicorn_scripts/gen_ca_https_key.sh
	echo "If gunicorn fails to start but nginx starts try rerunning the systemd_setup.sh script, then teardown and redeploy."
teardown:
	# reset database
	python3 delete_db_and_data.py
	# reset virtual environment
	nginx_venv_gunicorn_scripts/venv_reset.sh
	# reset keys
	#rm -f private_key.pem 
	#rm -f certificate.pem
	# reset systemd
	@ nginx_venv_gunicorn_scripts/systemd_reset.sh
	# reset nginx
	@ nginx_venv_gunicorn_scripts/nginx_reset.sh
