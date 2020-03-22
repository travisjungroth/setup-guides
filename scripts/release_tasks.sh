#!/bin/bash
set -e
python manage.py migrate --noinput
if [ -z "$HEROKU_SLUG_COMMIT" ]
then
  echo "Installing sentry-cli"
  curl -sL https://sentry.io/get-cli/ | bash
  echo "Making release"
  sentry-cli releases new -p starter "$HEROKU_SLUG_COMMIT"
  sentry-cli releases set-commits "$HEROKU_SLUG_COMMIT" -c "travisjungroth/starter@$HEROKU_SLUG_COMMIT"
  sentry-cli releases finalize "$HEROKU_SLUG_COMMIT"
  sentry-cli releases deploys "$HEROKU_SLUG_COMMIT" new -e "$HEROKU_APP_NAME" -n "$HEROKU_APP_NAME-$HEROKU_RELEASE_VERSION"
fi
