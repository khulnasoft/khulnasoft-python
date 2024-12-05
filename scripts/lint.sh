#!/usr/bin/env bash

set -e
set -x

mypy khulnasoft
ruff check khulnasoft tests scripts
ruff format khulnasoft tests --check