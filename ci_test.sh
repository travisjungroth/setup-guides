#!/bin/bash
set -e
pytest --cov-report xml --cov=.
