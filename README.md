# artworkcompetition
Artwork Competition web application built with django

## Demo screenshots
![alt text](https://raw.githubusercontent.com/amirashoori7/artworkcompetition/master/demo/demo1.png)
![alt text](https://raw.githubusercontent.com/amirashoori7/artworkcompetition/master/demo/demo2.png)
![alt text](https://raw.githubusercontent.com/amirashoori7/artworkcompetition/master/demo/work_lists.png)
![alt text](https://raw.githubusercontent.com/amirashoori7/artworkcompetition/master/demo/REST_API.png)


## Getting started
create python virtual environment

```bash
pip install virtualenv
virtualenv --python=python3 envname
cd envname
source bin/activate
```

## install django and other required packages using pip
all the required packages are included in the requirements.txt file and you can install all of them at once
pinning down the installed packages and application dependencies, and to install them in other environments
```bash
pip freeze > requirements.txt
pip install -r requirements.txt
```
to manually install packages
```bash
pip install django
pip install djangorestframework
pip install pillow
pip install psycopg2-binary
pip install python-dateutil
pip install sqlparse
```

## start django project and start builing new apps in it

```bash
django-admin startproject myproject
cd myproject
django-admin startapp myapp
```
## create db, db user and password and add the db settings in project's settings.py file

## crontab for auto db and media backups
backing up db every day at midnight to a folder
```bash
sudo crontab -e
0 0 * * * sudo PGPASSWORD="PASSWORD" pg_dump -U USERNAME -h HOST NAME_OF_DB > LOCATION_AND_NAME_OF_BACKUP_FILE
```
to automate rclone first we make a shell script and make it executable
for our purpose we have 2 rclone shells, one for media folder and another for database dumps
```bash
nano rclone-cron.sh
chmod a+x rclone-cron.sh

crontab -e
0 0 * * * /path/rclone-cron.sh >/dev/null 2>&1
```


##Update:
1- to login as root:
	sudo -s
2- go to the production folder and activate the virtual environment:
	source bin/activate

3- to remove the migration folders:
	a) cd artworkcompetition
	b) rm -r account/migrations
	c) rm -r evaluation/migrations
	d) rm -r artwork/migrations

4- to pull entire the project, go to the production folder
 git clone https://github.com/amirashoori7/artworkcompetition.git
 git checkout AmirS
 git pull
5- to change the mathart/settings.py
nano settings.py
change the database name
username: mathartuser
password: mathartuser

6- to fix the database:
drop database mathart;
create database mathart;
grant all on database mathart to mathartuser;

7- in the production/artworkcompetition folder to manage the DJango artwork competition folder
./manage.py


8- to manage nginx and GUnicorn:
	a. systemctl restart gunicorn.socket
	b. systemctl restart gunicorn.service
	c. service nginx restart


To make a backup:
./manage.py dbbackup
./manage.py mediabackup



Postgres Commands>>>

psql mathartuser -h 127.0.0.1 -d mathart

SELECT * FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema';

SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_NAME = 'account_projectuser';

DROP TABLE films, distributors;

CREATE TABLE account(
   id serial PRIMARY KEY,
   username VARCHAR (50) UNIQUE NOT NULL,
   password VARCHAR (50) NOT NULL,
   email VARCHAR (355) UNIQUE NOT NULL,
   created_on TIMESTAMP NOT NULL,
   last_login TIMESTAMP
);

