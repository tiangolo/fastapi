#!/usr/bin/env bash

set -e
set -x

mypy fastapi
black fastapi tests --check
isort --multi-line=3 --trailing-comma --force-grid-wrap=0 --combine-as --line-width 88 --fas --check-only --thirdparty fastapi --thirdparty fastapi --thirdparty pydantic --thirdparty starlette fastapi tests
