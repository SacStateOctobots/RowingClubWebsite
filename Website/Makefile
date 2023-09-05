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
	./gen_https_key.sh
reset_selfsign_keys:
	rm private_key.pem 
	rm certificate.pem
