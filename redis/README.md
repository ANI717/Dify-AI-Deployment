# Redis

#### Create Volume
```bash
docker volume create redis-volume
```

#### Remove Previous Leftovers
```bash
docker rm -f redis
docker run --rm -v redis-volume:/mnt alpine sh -lc "rm -rf /mnt/redis-data/*"
```

#### Deploy Redis Container
```bash
docker run -d --name redis -p 6379:6379 -v redis-volume:/tmp/redis-data redis:7-alpine sh -c 'mkdir -p /tmp/redis-data && chown -R redis:redis /tmp/redis-data && exec redis-server --appendonly yes --dir /tmp/redis-data'
```

#### Test with Python
```bash
pip install psycopg2-binary dotenv
python .\test_redis.py
```
