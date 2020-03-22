#!/bin/bash
set -e
python manage.py migrate --noinput
if [ -z "$HEROKU_SLUG_COMMIT" ]
then
  curl -sL https://sentry.io/get-cli/ | bash
  sentry-cli releases new -p starter "$HEROKU_SLUG_COMMIT"
  sentry-cli releases set-commits -c "$HEROKU_SLUG_COMMIT"
  sentry-cli releases finalize "$HEROKU_SLUG_COMMIT"
  sentry-cli releases deploys "$HEROKU_SLUG_COMMIT" new -e "$HEROKU_APP_NAME"
fi
