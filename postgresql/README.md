# PostgreSQL

#### Create Volume
```bash
docker volume create postgres-volume
```

#### Remove Previous Leftovers
```bash
docker rm -f postgres
docker run --rm -v postgres-volume:/var/lib/postgresql/data alpine sh -lc "rm -rf /var/lib/postgresql/data/* /var/lib/postgresql/data/..?* /var/lib/postgresql/data/.[!.]*"
```

#### Deploy PostgreSQL Container
```bash
docker run -d --name postgres --env-file .env --read-only --tmpfs /var/run/postgresql:rw,mode=1777 --tmpfs /tmp:rw,mode=1777 -v postgres-volume:/var/lib/postgresql/data:rw -v "${PWD}/postgresql.conf:/etc/postgresql/postgresql.conf:ro" -v "${PWD}/pg_hba.conf:/etc/postgresql/pg_hba.conf:ro" -p 5432:5432 postgres:17-alpine -c config_file=/etc/postgresql/postgresql.conf -c hba_file=/etc/postgresql/pg_hba.conf
```

#### Connect to PostgreSQL
```bash
docker exec -it postgres psql -U appuser -d appdb
```

#### Connect from Remote Device
```bash
psql -h localhost:5432 -U appuser -d appdb
```

#### Test with Python
```bash
pip install psycopg2-binary dotenv
python .\test_with_psycopg2.py
python .\test_with_sqlalchemy.py
```
