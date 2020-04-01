#!/bin/bash
set -e
python manage.py migrate --noinput
if [ -n "$HEROKU_SLUG_COMMIT" ]
then
  export INSTALL_DIR=/app
  curl -sL https://sentry.io/get-cli/ | bash
  ./sentry-cli releases new -p "highly-composite" "$HEROKU_SLUG_COMMIT"
  ./sentry-cli releases set-commits "$HEROKU_SLUG_COMMIT" -c "highlycomposite/highlycomposite@$HEROKU_SLUG_COMMIT"
  ./sentry-cli releases finalize "$HEROKU_SLUG_COMMIT"
  ./sentry-cli releases deploys "$HEROKU_SLUG_COMMIT" new -e "$HEROKU_APP_NAME" -n "$HEROKU_APP_NAME-$HEROKU_RELEASE_VERSION"
fi
