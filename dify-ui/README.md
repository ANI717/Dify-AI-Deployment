# Dify API
Reference: https://github.com/langgenius/dify/tree/main/web

#### Create Volume
```bash
docker volume create tmpui
```

#### Build & run (read-only root + writable /tmp + .env)
```bash
docker build -t dify-ui-image:latest -f Dockerfile .
docker run -d --name dify-ui --read-only -v tmpui:/tmp --env-file .env -p 8888:8080 dify-ui-image:latest
```