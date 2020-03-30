# Highly Composite
The problem we're trying to solve is how hard it is for junior software engineers to contribute. How we'll do that is [unsure](https://github.com/highlycomposite/highlycomposite/wiki/Roadmap). Here's how [you can help](https://github.com/highlycomposite/highlycomposite/blob/master/CONTRIBUTING.md).

### [Setup Instructions](/SETUP.md) 

### Tests
#### Running  

    pytest
    
#### With coverage

    pytest --cov=.
    
#### Recreate the test database (runs migrations)

    pytest --create-db test_basics.py::test_database

### Server
    
    ./manage.py runserver

Set DEBUG=true in .env to run the server in debug mode.

### Deployment
The master branch autodeploys to a Heroku [staging environment](https://highly-composite-staging.herokuapp.com/). Production doesn't exist (yet). New PRs automatically create a review app. Here's the full [deployment list](https://github.com/highlycomposite/highlycomposite/deployments).
