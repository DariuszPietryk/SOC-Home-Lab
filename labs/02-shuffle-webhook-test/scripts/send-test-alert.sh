#!/usr/bin/env bash
set -euo pipefail

: "${SHUFFLE_WEBHOOK_URL:?Set SHUFFLE_WEBHOOK_URL to your PRIVATE webhook URL; do not commit it}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PAYLOAD="${SCRIPT_DIR}/../examples/simulated-wazuh-alert.json"

case "$SHUFFLE_WEBHOOK_URL" in
  http://127.0.0.1:*|http://localhost:*|http://172.16.*|http://192.168.*|http://10.*) ;;
  *) echo 'Refusing URL outside common local lab addresses. Review destination before sending.' >&2; exit 2 ;;
esac

curl --fail-with-body --show-error --silent --include \
  --connect-timeout 5 --max-time 30 \
  --request POST "$SHUFFLE_WEBHOOK_URL" \
  --header 'Content-Type: application/json' \
  --data-binary "@$PAYLOAD"
printf '\n'
