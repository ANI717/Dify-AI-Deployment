# Dify API
Reference: https://github.com/langgenius/dify/tree/main/web

#### Build & run (read-only root + writable /tmp + .env)
```bash
docker build -t dify-ui-image:latest -f Dockerfile .
docker volume create tmp
docker run --name dify-ui --read-only --mount type=volume,src=tmp,dst=/tmp --env-file .env -p 8080:8080 dify-ui-image:latest
```