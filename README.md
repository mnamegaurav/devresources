# devresources
One destination for all the developer's learning resources.

### Live -
https://devresources-guru.herokuapp.com/

### Contributing

To install this project locally and imporove it:

Create a python3 virtual environment.

```
python3 -m venv venv
```

Or, use [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html):

```
virtualenv venv
```

### Install requirements

```
. venv/bin/activate
pip install -r requirements.txt
```

Errors during install help:

- `Error: pg_config executable not found.` *and* you are using ubuntu

You need to install Postgress & dev headers: `sudo apt install -y postgresql-client postgresql libpq-dev`

- './psycopg/psycopg.h:36:10: fatal error: libpq-fe.h: No such file or directory'


### Create database user

Example using postgress locally: [configure pg_hba.conf correctly](https://www3.ntu.edu.sg/home/ehchua/programming/sql/PostgreSQL_GetStarted.html#:~:text=To%20test%20the%20password%20login,prompt%20you%20for%20the%20password.) Or use sqlite

```
sudo su postgresql
createdb devresources
createuser -P -s -e devresources # Warning! this creates a superuser
```

### Copy .env.example to .env

```
cp .env.example to .env
```
**Change** the .env settings to your database username/password

### Run database migrations
```
python manage.py migrate
```

### Seed the database

See / insert database with inital values

```
python manage.py loaddata devresources/fixtures/ResourceCategory.yaml
```


### Run the application

```
python manage.py runserver
```

Visit http://127.0.0.1:8000/
