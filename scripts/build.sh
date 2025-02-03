#!/bin/bash

poetry install
poetry run black .
poetry run isort .
poetry version patch
poetry run pytest
poetry build
