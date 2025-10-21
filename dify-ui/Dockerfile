# base image
FROM node:22-slim AS base

RUN apt-get install -y tzdata
RUN corepack enable
ENV PNPM_HOME="/tmp/pnpm"
ENV PATH="$PNPM_HOME:$PATH"
ENV NEXT_PUBLIC_BASE_PATH=


# install packages
FROM base AS packages

WORKDIR /app/web

COPY package.json .
COPY pnpm-lock.yaml .

# Use packageManager from package.json
RUN corepack install

RUN pnpm install --frozen-lockfile

# build resources
FROM base AS builder
WORKDIR /app/web
COPY --from=packages /app/web/ .
COPY . .

ENV NODE_OPTIONS="--max-old-space-size=4096"
RUN pnpm build:docker


# production stage
FROM base AS production

ENV NODE_ENV=production
ENV EDITION=SELF_HOSTED
ENV DEPLOY_ENV=PRODUCTION
ENV CONSOLE_API_URL=http://127.0.0.1:8080
ENV APP_API_URL=http://127.0.0.1:8081
ENV MARKETPLACE_API_URL=https://marketplace.dify.ai
ENV MARKETPLACE_URL=https://marketplace.dify.ai
ENV PORT=8080
ENV NEXT_TELEMETRY_DISABLED=1
ENV PM2_INSTANCES=2

# set timezone
ENV TZ=UTC


WORKDIR /app/web
COPY --from=builder /app/web/public ./public
COPY --from=builder /app/web/.next/standalone ./
COPY --from=builder /app/web/.next/static ./.next/static

COPY docker/entrypoint.sh ./entrypoint.sh


# global runtime packages
RUN pnpm add -g pm2 \
    && mkdir -p /tmp/.pm2 /tmp/.cache/corepack /tmp/.cache/node \
    && chown -R 1001:0 /tmp/.pm2 /tmp/.cache /app/web \
    && chmod -R g=u /tmp/.pm2 /tmp/.cache /app/web \
    && chown -R 1001:0 /tmp/pnpm \
    && chmod -R a+rx /tmp/pnpm \
    && chmod +x /app/web/entrypoint.sh \
    && find /tmp/pnpm -name "pm2" -type f -exec chmod +x {} \;


ARG COMMIT_SHA
ENV COMMIT_SHA=${COMMIT_SHA}

USER 1001
EXPOSE 8080
ENTRYPOINT ["/bin/bash","./entrypoint.sh"]
