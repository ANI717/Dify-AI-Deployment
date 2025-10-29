# syntax=docker/dockerfile:1
FROM python:3.12-slim-bullseye AS builder

ARG VERSION=unknown
ARG GO_VERSION=1.23.2

# Install Go in builder stage
RUN apt-get update && \
    apt-get install -y curl && \
    curl -fsSL "https://go.dev/dl/go${GO_VERSION}.linux-amd64.tar.gz" -o /tmp/go.tgz && \
    tar -C /usr/local -xzf /tmp/go.tgz && \
    rm /tmp/go.tgz && \
    apt-get remove -y curl && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

ENV PATH="/usr/local/go/bin:${PATH}"

# copy project
COPY . /app

# set working directory
WORKDIR /app

# using goproxy if you have network issues
# ENV GOPROXY=https://goproxy.cn,direct

# build
RUN /usr/local/go/bin/go build \
    -ldflags "\
    -X 'github.com/langgenius/dify-plugin-daemon/internal/manifest.VersionX=${VERSION}' \
    -X 'github.com/langgenius/dify-plugin-daemon/internal/manifest.BuildTimeX=$(date -u +%Y-%m-%dT%H:%M:%S%z)'" \
    -o /app/main cmd/server/main.go

# copy entrypoint.sh
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

FROM python:3.12-slim-bullseye

WORKDIR /app

# check build args
ARG PLATFORM=local

# Install additional packages for Python dependencies
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    curl ffmpeg build-essential git cmake pkg-config \
    libcairo2-dev libjpeg-dev libgif-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Configure all caches and writable directories to use /tmp
ENV TIKTOKEN_CACHE_DIR=/tmp/.tiktoken \
    XDG_CACHE_HOME=/tmp/.cache \
    PIP_CACHE_DIR=/tmp/pip-cache \
    PYTHONPYCACHEPREFIX=/tmp/pycache \
    TMPDIR=/tmp \
    HOME=/tmp \
    VIRTUAL_ENV=/tmp/venv

# Install dify_plugin to speedup the environment setup, test uv and preload tiktoken
RUN python3 -m pip install uv && \
    uv pip install --system dify_plugin && \
    python3 -c "from uv._find_uv import find_uv_bin;print(find_uv_bin());" && \
    python3 -c "import tiktoken; encodings = ['o200k_base', 'cl100k_base', 'p50k_base', 'r50k_base', 'p50k_edit', 'gpt2']; [tiktoken.get_encoding(encoding).special_tokens_set for encoding in encodings]"

ENV UV_PATH=/usr/local/bin/uv
ENV PLATFORM=$PLATFORM
ENV GIN_MODE=release

# Expose the application port
EXPOSE 5002

# Declare /tmp as a writable volume
VOLUME ["/tmp"]

COPY --from=builder /app/main /app/entrypoint.sh /app/

# run the server, using sh as the entrypoint to avoid process being the root process
# and using bash to recycle resources
CMD ["/bin/bash", "-c", "/app/entrypoint.sh"]
