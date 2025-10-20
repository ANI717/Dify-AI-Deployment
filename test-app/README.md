Create Virtual Environment
```
python -m venv .venv
```

Generate a lock file locally
```
pip install uv
uv lock
```

Build & run (read-only root + writable /tmp + .env)
```
docker build -t test-app:latest -f Dockerfile .
docker volume create tmp
docker run --name fastapi-ro --read-only --mount type=volume,src=tmp,dst=/tmp --env-file .env -p 8080:8080 test-app:latest &
```