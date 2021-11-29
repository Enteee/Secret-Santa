#!/usr/bin/env bash
set -exuo pipefail

SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
IMAGE="$(docker build -q "${SCRIPT_DIR}")"

PORT="42418"

docker run \
  -p "${PORT}:${PORT}" \
  "${IMAGE}" \
    "secretsanta.py" \
      --port "${PORT}" \
      "$@"
