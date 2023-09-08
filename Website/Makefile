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
	./gen_selfsign_https_key.sh
reset_selfsign_keys:
	sudo rm -f private_key.pem 
	sudo rm -f certificate.pem
deploy:
	# setup database
	python3 setup_database.py
	# set up virtual environment
	nginx_venv_gunicorn_scripts/venv_setup.sh
	# set up keys
	./gen_selfsign_https_key.sh
	# set up systemd
	nginx_venv_gunicorn_scripts/systemd_setup.sh
teardown:
	# setup database
	python3 delete_db_and_data.py
	# set up virtual environment
	nginx_venv_gunicorn_scripts/venv_reset.sh
	# set up keys
	rm -f private_key.pem 
	rm -f certificate.pem
	# set up systemd
	nginx_venv_gunicorn_scripts/systemd_reset.sh
