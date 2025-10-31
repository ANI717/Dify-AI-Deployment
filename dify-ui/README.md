# Dify API
Reference: https://github.com/langgenius/dify/tree/main/web

#### Remove Previous Leftovers
```bash
docker rm -f dify-ui
```

#### Create Volume
```bash
docker volume create dify-ui-volume
```

#### Build Image
```bash
docker build -t dify-ui-image:latest -f Dockerfile .
```

### Run Container
```bash
docker run -d --name dify-ui --read-only -v dify-ui-volume:/tmp --env-file .env -p 3000:3000 dify-ui-image:latest
```
