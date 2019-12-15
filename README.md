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
