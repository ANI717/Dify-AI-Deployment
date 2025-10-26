# Dify Worker
Reference: https://github.com/langgenius/dify/tree/main/api

#### Remove Previous Leftovers
```bash
docker rm -f dify-worker
```

#### Build Image
```bash
docker build -t dify-api-image:latest -f Dockerfile .
```

#### Run Container
```bash
docker run -d --name dify-worker --read-only -v dify-api-volume:/tmp --env-file .env dify-api-image:latest
```
