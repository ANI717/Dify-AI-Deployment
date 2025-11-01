#!/bin/bash
export TIKTOKEN_CACHE_DIR=/tmp/.tiktoken

# Create necessary directories in /tmp (in case they don't exist from volume mount)
mkdir -p /tmp/.tiktoken /tmp/storage /tmp/logs /tmp/python-packages \
    /tmp/.cache /tmp/uv-cache /tmp/plugins /tmp/plugins/installed /tmp/plugins/packages

exec /app/main
