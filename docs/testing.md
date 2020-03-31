# Testing
Make sure either a virtual environment is active (use `pipenv shell`), or prepend each command here with `pipenv run`.

## Running tests

    pytest
    
## With coverage

    pytest --cov=.
    
## Recreate the test database (runs the migrations)
By default, the test database is reused for every run. You can create a new one each time with:

    pytest --create-db
    
If you want to just recreate the database and run a single test so you can go back to normal use (good for handling a new migration) run:

    pytest --create-db test_basics.py::test_database
    
