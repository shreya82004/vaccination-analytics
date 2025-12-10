from src.config import get_connection_string
from sqlalchemy import create_engine

conn_str = get_connection_string()
print("Connection string:", conn_str)

try:
    engine = create_engine(conn_str)
    with engine.connect() as conn:
        print("✅ Connected successfully!")
except Exception as e:
    print("❌ Connection error:", e)
