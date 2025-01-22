#!/bin/bash

poetry install
poetry run black .
poetry run isort .
poetry version patch
poetry build
poetry config pypi-token.pypi $PYPI_TOKEN
poetry publish --build
