# Running
Make sure either a virtual environment is active (use `pipenv shell`), or prepend each command here with `pipenv run`.

### Server
For local development use the built in Django [development server](https://docs.djangoproject.com/en/3.0/ref/django-admin/#runserver). 

    ./manage.py runserver
   
#### Debug mode
`scripts/setup.sh` added `DJANGO_DEBUG=true` to your .env file, making the server run in [debug mode](https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-DEBUG), which you probably want for development.

#### Non-debug mode
To take the server out of debug mode, remove the `DJANGO_DEBUG` line or set it to "false". Out of debug mode, you'll need manually handle the [static files](https://docs.djangoproject.com/en/3.0/ref/contrib/staticfiles/).
    
    ./manage.py collectstatic
