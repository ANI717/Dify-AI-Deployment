# Dify API
Reference: https://github.com/langgenius/dify/tree/main/api

#### Create Virtual Environment
```bash
python -m venv .venv
```

#### Generate a UV lock file locally
```bash
pip install uv
uv lock
```

#### Create Volume
```bash
docker volume create tmp
```

#### Build & run (read-only root + writable /tmp + .env)
```bash
docker build -t dify-api-image:latest -f Dockerfile .
docker run -d --name dify-api --read-only --mount type=volume,src=tmp,dst=/tmp --env-file .env -p 5001:8080 dify-api-image:latest
```