#!/usr/bin/env bash
set -exuo pipefail

SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

PORT="42418"

TLS_KEY="${TLS_KEY:-./key.pem}"
if [ ! -f "${TLS_KEY}" ]; then
  1>&2 echo "TLS_KEY (= '${TLS_KEY}') is not a file"
  exit 1
fi

TLS_CERT="${TLS_CERT:-./cert.pem}"
TLS_CERT=$(realpath "${TLS_CERT}")
if [ ! -f "${TLS_CERT}" ]; then
  1>&2 echo "TLS_CERT (= '${TLS_CERT}') is not a file"
  exit 1
fi

IMAGE="$(docker build -q "${SCRIPT_DIR}")"


docker run \
  --volume "$(realpath "${TLS_CERT}"):/cert:ro" \
  --volume "$(realpath "${TLS_KEY}"):/key:ro" \
  -p "${PORT}:${PORT}" \
  "${IMAGE}" \
    "secretsanta.py" \
      --port "${PORT}" \
      --tls-cert "/cert" \
      --tls-key "/key" \
      "$@"
