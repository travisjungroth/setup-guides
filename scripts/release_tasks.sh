#!/bin/bash
python manage.py migrate --noinput || exit
VERSION=$(sentry-cli releases propose-version)
sentry-cli releases new -p starter "$VERSION"
sentry-cli releases set-commits --auto "$VERSION"

