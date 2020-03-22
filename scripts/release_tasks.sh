#!/bin/bash
python manage.py migrate --noinput || exit
if [ -n "$REVIEW_APP" ] && [ -n "$CI" ]
then
  curl -sL https://sentry.io/get-cli/ | bash
  sentry-cli releases new -p starter "$HEROKU_SLUG_COMMIT"
  sentry-cli releases set-commits --auto "$HEROKU_SLUG_COMMIT"
  sentry-cli releases finalize "$HEROKU_SLUG_COMMIT"
fi
