FROM golang:1.23-alpine AS builder

ARG VERSION=unknown

# copy project
COPY . /app

# set working directory
WORKDIR /app

# using goproxy if you have network issues
# ENV GOPROXY=https://goproxy.cn,direct

# build
RUN go build \
    -ldflags "\
    -X 'github.com/langgenius/dify-plugin-daemon/internal/manifest.VersionX=${VERSION}' \
    -X 'github.com/langgenius/dify-plugin-daemon/internal/manifest.BuildTimeX=$(date -u +%Y-%m-%dT%H:%M:%S%z)'" \
    -o /app/main cmd/server/main.go

# copy entrypoint.sh
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

FROM python:3.12-slim-bookworm

WORKDIR /app

# check build args
ARG PLATFORM=local

# Install additional packages needed for the application
RUN set -ex && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y curl \
        python3-dev python3-pip ffmpeg \
        build-essential git \
        cmake pkg-config \
        libcairo2-dev libjpeg-dev libgif-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install dify_plugin to speedup the environment setup, test uv and preload tiktoken
RUN set -ex && \
    rm -f /usr/lib/python*/EXTERNALLY-MANAGED && \
    python3 -m pip install uv && \
    uv pip install --system dify_plugin && \
    python3 -c "from uv._find_uv import find_uv_bin;print(find_uv_bin());" && \
    python3 -c "import tiktoken; encodings = ['o200k_base', 'cl100k_base', 'p50k_base', 'r50k_base', 'p50k_edit', 'gpt2']; [tiktoken.get_encoding(encoding).special_tokens_set for encoding in encodings]"

ENV UV_PATH=/usr/local/bin/uv
ENV PLATFORM=$PLATFORM
ENV GIN_MODE=release
ENV PLUGIN_REMOTE_INSTALLING_ENABLED=false

# Plugin configuration for local platform
ENV PLUGIN_WORKING_PATH=/tmp/plugins
ENV PLUGIN_INSTALLED_PATH=/tmp/plugins/installed
ENV PLUGIN_PACKAGE_CACHE_PATH=/tmp/plugins/packages

# Configure Python to install packages in /tmp for runtime installations
ENV PYTHONPATH=""
ENV PYTHONUSERBASE=/tmp/python-packages
ENV PIP_USER=1
ENV PYTHONPATH=/tmp/python-packages/lib/python3.12/site-packages:$PYTHONPATH

# Create a non-root user
RUN groupadd -r dify && useradd -r -g dify -u 1001 dify

# Create necessary directories in tmp for write access
RUN mkdir -p /tmp/.tiktoken /tmp/storage /tmp/logs /tmp/python-packages \
    /tmp/plugins /tmp/plugins/installed /tmp/plugins/packages && \
    chmod -R 755 /tmp/.tiktoken /tmp/storage /tmp/logs /tmp/python-packages \
    /tmp/plugins /tmp/plugins/installed /tmp/plugins/packages

COPY --from=builder /app/main /app/entrypoint.sh /app/

# Set ownership of the application files and directories to the dify user
RUN chown -R dify:dify /app /tmp/.tiktoken /tmp/storage /tmp/logs /tmp/python-packages \
    /tmp/plugins /tmp/plugins/installed /tmp/plugins/packages

# Change working directory to /tmp so the app creates storage there
WORKDIR /tmp

# Switch to non-root user
USER dify

# run the server, using sh as the entrypoint to avoid process being the root process
# and using bash to recycle resources
CMD ["/bin/bash", "-c", "/app/entrypoint.sh"]
