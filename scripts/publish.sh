#!/bin/bash

poetry build
poetry config pypi-token.pypi $PYPI_TOKEN
poetry publish --build
