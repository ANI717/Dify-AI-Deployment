import psycopg2
import os

# Load environment variables if needed (optional if you want to reuse your .env)
from dotenv import load_dotenv
load_dotenv(".env")

# Fetch connection details from .env
db_user = os.getenv("POSTGRES_USER", "appuser")
db_password = os.getenv("POSTGRES_PASSWORD", "strongpassword")
db_name = os.getenv("POSTGRES_DB", "appdb")
db_host = os.getenv("POSTGRES_HOST", "localhost")  # default for local Docker
db_port = os.getenv("POSTGRES_PORT", "5432")

try:
    conn = psycopg2.connect(
        host=db_host,
        port=db_port,
        user=db_user,
        password=db_password,
        dbname=db_name,
    )
    print("✅ Connection successful!")

    # Create a cursor to run SQL
    cur = conn.cursor()
    cur.execute("SELECT version();")
    version = cur.fetchone()
    print("PostgreSQL version:", version)

    # Optionally test insert/select
    cur.execute("CREATE TABLE IF NOT EXISTS test_table (id SERIAL PRIMARY KEY, name TEXT);")
    cur.execute("INSERT INTO test_table (name) VALUES ('Hello from Python') RETURNING id;")
    new_id = cur.fetchone()[0]
    print("Inserted row ID:", new_id)

    conn.commit()
    cur.execute("SELECT * FROM test_table;")
    print("Rows:", cur.fetchall())

    cur.close()
    conn.close()

except Exception as e:
    print("❌ Connection failed:", e)
