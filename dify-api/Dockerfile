# ---------- Base Stage ----------
FROM python:3.11-slim-bullseye AS base

# Set working directory
WORKDIR /app/api

# Install uv
ENV UV_VERSION=0.9.5
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir uv==${UV_VERSION}


# ---------- Packages Stage ----------
FROM base AS packages

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc g++ libc-dev libffi-dev libgmp-dev libmpfr-dev libmpc-dev

# Install Python dependencies
COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-dev


# ---------- Production Stage ----------
FROM base AS production

# Set environment variables
ENV FLASK_APP=app.py
ENV EDITION=SELF_HOSTED
ENV DEPLOY_ENV=PRODUCTION

ENV CONSOLE_API_URL=http://127.0.0.1:5001
ENV CONSOLE_WEB_URL=http://127.0.0.1:8080
ENV SERVICE_API_URL=http://127.0.0.1:5001
ENV APP_WEB_URL=http://127.0.0.1:8080

ENV DIFY_BIND_ADDRESS=0.0.0.0
ENV DIFY_PORT=8080

ENV TZ=UTC

ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8
ENV PYTHONIOENCODING=utf-8

# Set working directory
WORKDIR /app/api

# Install system dependencies
RUN \
    apt-get update \
    && apt-get install -y --no-install-recommends \
        # basic environment
        curl libgmp-dev libmpfr-dev libmpc-dev \
        # For Security
        expat libldap-2.4-2 libldap2-dev perl libsqlite3-0 zlib1g \
        # install fonts to support the use of tools like pypdfium2
        fonts-noto-cjk \
        # install a package to improve the accuracy of guessing mime type and file extension
        media-types \
        # install libmagic to support the use of python-magic guess MIMETYPE
        libmagic1 \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy Python environment and packages
ENV VIRTUAL_ENV=/app/api/.venv
COPY --from=packages ${VIRTUAL_ENV} ${VIRTUAL_ENV}
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"

# copy vendored NLTK data
COPY nltk_data /usr/local/share/nltk_data
ENV NLTK_DATA=/usr/local/share/nltk_data

# Copy source code
COPY . /app/api/

# Copy entrypoint
COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ARG COMMIT_SHA
ENV COMMIT_SHA=${COMMIT_SHA}

# Expose port
EXPOSE 8080

# Set entrypoint
ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]
