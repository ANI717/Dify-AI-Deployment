# Dify API
Reference: https://github.com/langgenius/dify/tree/main/web

#### Remove Previous Leftovers
```bash
docker rm -f dify-plugin
```

#### Build Image
```bash
docker build -t dify-plugin-image:latest -f Dockerfile .
```

### Run Container
```bash
docker run -d --name dify-plugin --read-only -v dify-ui-plugin:/tmp --env-file .env -p 5002:5002 dify-plugin-image:latest
```
