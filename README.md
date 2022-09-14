# ninerogues_ecommerce_testing
Developing automation tests to the ecommerce of ninerogues project 

## Install Project

#### Setup Postgres Database

(on server: psql -h <ip> -U root -d postgres)
```
sudo su postgres -c psql
```
```
CREATE USER testing_user WITH PASSWORD 'testing_password';
CREATE DATABASE testing_db OWNER testing_user;
GRANT ALL PRIVILEGES ON DATABASE testing_db TO testing_user;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO testing_user;
ALTER USER testing_user CREATEDB;
ALTER ROLE testing_user SUPERUSER;
\q
```