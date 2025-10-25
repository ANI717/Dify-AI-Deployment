import os
from urllib.parse import quote_plus
from sqlalchemy import create_engine, text

# Load environment variables if needed
from dotenv import load_dotenv
load_dotenv(".env")

# Fetch connection details from .env
db_user = os.getenv("POSTGRES_USER", "appuser")
db_password = os.getenv("POSTGRES_PASSWORD", "strongpassword")
db_name = os.getenv("POSTGRES_DB", "appdb")
db_host = os.getenv("POSTGRES_HOST", "localhost")  # default for local Docker
db_port = os.getenv("POSTGRES_PORT", "5432")

# Connection string
db_uri = f"postgresql+psycopg2://{quote_plus(db_user)}:{quote_plus(db_password)}@{quote_plus(db_host)}:{quote_plus(db_port)}/{quote_plus(db_name)}"

# Create engine and connect
engine = create_engine(db_uri)

with engine.connect() as conn:
    result = conn.execute(text("SELECT version();"))
    print(result.fetchone())
