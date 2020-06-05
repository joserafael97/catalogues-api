![Django CI](https://github.com/joserafael97/catalogues-api/workflows/Django%20CI/badge.svg?branch=master)
# Catalogues-api
API RESTful for managing vendors and products.

## Deployed links app

* [API docs](https://catalogues-api.herokuapp.com)
* [Main end-point](https://catalogues-api.herokuapp.com/api/vendors)
* [Front-end deployed](https://catalogues-ui.herokuapp.com)

## Getting Started
This project was developed on the Python language with the [Django](https://github.com/django) framework with the help of the [django-rest-framework](https://www.django-rest-framework.org/).


### Estructure
The project directory structure is described below

```bash
.
├── .github/workflows                 # Stores file that triggers Github Action;
├── api/...                           # Files containing API logic with routes to access vendors;
├── catalogues/                       # Config files Django;
      ├── settings/...                # Config files environment;
      ├── ...                         # All files config;
├── .env                              # Config file environment in develop mode;
├── Dockerfile                        # Dockerfile to deploy;
├── manage.py                         # Init config and run in develop mode;
└── requirements.txt                  # Project dependecies.
```

### Prerequisites
For the execution of the project, it is necessary to install the following tools

* Python 3 (used v3.8)
* pip
* PostgresSql (used v11.x)

### Installing
To install the libraries, run the command below inside the main repository directory.

```
pip install -r requirements.txt
```

Besides, it is necessary to change the values of the variables defined in the [.env](https://github.com/joserafael97/catalogues-api/blob/master/.env) file located at the root of the project with their credentials for accessing the database, below it is an example:

```
SECRET_KEY_DEV=u!j$-o!5%3_5b97o^cmerce0koj!bkblzgs+bxg7p^zrywmsft
DB_NAME_DEV=catalogues
DB_USER_DEV=django
DB_PASSWORD_DEV=devenv
HOST_DEV=localhost
PORT_DEV=5432
DEBUG_DEV=True
```

To create the database tables, in terminal run:

```
python manage.py makemigraions && python manage.py makemigraions 
```

### Run API

```
python manage.py runserver
```

## Run API with diff environment config
for the management of the different environments of the project, were specific files that add certain specificities:

* [development](https://github.com/joserafael97/catalogues-api/blob/master/catalogues/settings/development.py) (default)
* [tester](https://github.com/joserafael97/catalogues-api/blob/master/catalogues/settings/tester.py) (use Sqlite)
* [production](https://github.com/joserafael97/catalogues-api/blob/master/catalogues/settings/production.py)

to run the service with one of the environments manually, you can do, for example:

```
python manage.py runserver --settings=catalogues.settings.tester 
```

This is valid to migration operation and all in manage.py file.


### Automatic Deploy
This project uses Github Action to deploy the application to each new commit main branch. To do this, it uses the following file:

* [.github/workflows/django.yml](https://github.com/joserafael97/catalogues-api/blob/master/.github/workflows/django.yml)


## Authors

* **José Remígio** - *Initial work* - [José Remígio](https://github.com/joserafael97)

[***License MIT***](https://github.com/joserafael97/auditor-crawler/blob/master/LICENSE)
