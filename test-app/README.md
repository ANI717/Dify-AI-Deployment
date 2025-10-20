#### Create Virtual Environment
```bash
python -m venv .venv
```

#### Generate a UV lock file locally
```bash
pip install uv
uv lock
```

#### Build & run (read-only root + writable /tmp + .env)
```bash
docker build -t test-app-image:latest -f Dockerfile .
docker volume create tmp
docker run --name test-app --read-only --mount type=volume,src=tmp,dst=/tmp --env-file .env -p 8080:8080 test-app-image:latest
```
