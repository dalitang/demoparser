#!/bin/bash
set -euo pipefail

PARSER_IMAGE=demo-parser:latest

docker run --rm \
    -v `pwd`:/app \
    ${PARSER_IMAGE} \
    python -m pytest ./tests/acceptance -vv
