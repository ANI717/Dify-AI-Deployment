# syntax=docker/dockerfile:1

############################
# Stage 1 — base (build)
############################
FROM python:3.11-slim-bullseye AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    HOME=/tmp

WORKDIR /app

# Install dependencies needed for certificates only (not for uv)
RUN apt-get update \
 && apt-get install -y --no-install-recommends ca-certificates \
 && rm -rf /var/lib/apt/lists/*

# Install uv from PyPI
RUN pip install --no-cache-dir uv

# Copy lockfiles first to maximize build caching
COPY pyproject.toml uv.lock ./

# Sync environment according to the lockfile
RUN uv sync --frozen --no-dev


############################
# Stage 2 — production (runtime)
############################
FROM python:3.11-slim-bullseye AS prod

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    HOME=/tmp \
    PATH="/app/.venv/bin:${PATH}"

WORKDIR /app

# Need ca-certificates at runtime for update-ca-certificates
RUN apt-get update \
 && apt-get install -y --no-install-recommends ca-certificates \
 && rm -rf /var/lib/apt/lists/*

# Copy virtualenv from base stage
COPY --from=base /app/.venv /app/.venv

# Install local certificates (no external downloads)
COPY certificates/*.crt /usr/local/share/ca-certificates/
RUN update-ca-certificates

# Copy app code
COPY app/ /app/

# Non-root user
RUN useradd -m -r -u 10001 appuser \
 && chown -R appuser:appuser /app
USER appuser

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
