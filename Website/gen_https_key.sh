#!/bin/bash
openssl req -x509 -nodes -days 3650 -newkey ec:<(openssl ecparam -name prime256v1) -keyout private_key.pem -out certificate.pem
