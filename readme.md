### Setup
Install postgres and pipenv if you haven't.
Run scripts/setup.sh from the base directory of the project.
Run pipenv install --dev  

### Tests
#### Running    
    pytest
    
#### With coverage

    pytest --cov=.
    
#### Recreate the database (runs migrations)

    pytest --create-db test_basics.py::test_database

### Server
#### Development
    
    ./manage.py runserver
    
#### Local Heroku
    
    heroku local
