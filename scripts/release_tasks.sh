#!/bin/bash
python manage.py migrate --noinput || exit
if [ -n "$CI" ]
# [ -n "$REVIEW_APP" ] &&
then
  VERSION=$(sentry-cli releases propose-version)
  sentry-cli releases new -p starter "$VERSION"
  sentry-cli releases set-commits --auto "$VERSION"
  sentry-cli releases finalize "$VERSION"
fi
