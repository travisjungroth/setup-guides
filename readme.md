### Setup
Install [Postgres](https://gist.github.com/ibraheem4/ce5ccd3e4d7a65589ce84f2a3b7c23a3) and [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/index.html#install-pipenv-today) if you don't have them.  
Run `scripts/setup.sh` from the base directory of the project.  
Run `pipenv install --dev` 

### Tests
#### Running    
    pytest
    
#### With coverage

    pytest --cov=.
    
#### Recreate the test database (runs migrations)

    pytest --create-db test_basics.py::test_database

### Server
#### Development
    
    ./manage.py runserver

Set DEBUG=true in .env for the debug server.
