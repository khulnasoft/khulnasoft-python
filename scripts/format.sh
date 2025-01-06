#!/usr/bin/env bash
set -x

ruff check khulnasoft tests scripts --fix
ruff format khulnasoft tests scripts
