# Job application Test.

## Write job Seraching Api user Flask , Flask-restful and Postgres. 

# setps to setup appliaation locally.

*Install Python 3.6 or above version.*

install virtualenv 
```
pip install virtualenv

* Creeate Virtualenv *

virtualenv venv

* acttivate virtualenv *

source venv/bin/activate

```

# installing requirements.txt file

```
pip install -r requirements.txt

```

## update .env file accourind to your configuration of database and application realted variable.

## Create migrations directory.

```
python manage.py db init

```

## repace src/extra.py files code into migrations/.env

### Migrate Database

```
python manage.py db migrate

** Update database and reflect the changes.

python manage.py db upgrade

```

## Run The Server 

```
flask run
```

### open the linke into borswer

[http://127.0.0.1:5000/](http://127.0.0.1:5000)

or swagger view

[http://localhost:5000/apidocs](http://localhost:5000/apidocs/#/default/post_api_login)

## Thanks & Regrads.

