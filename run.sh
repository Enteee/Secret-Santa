#!/usr/bin/env bash
set -exuo pipefail

SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
IMAGE="$(docker build -q "${SCRIPT_DIR}")"

PORT="$(shuf -i 1024-65535 -n 1)"

docker run \
  -p "${PORT}:${PORT}" \
  "${IMAGE}" \
    "secretsanta.py" \
      --print_host "${HOSTNAME}" \
      --port "${PORT}" \
      "$@"
