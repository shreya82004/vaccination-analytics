import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

DB_CONFIG = {
    'type': os.getenv('DB_TYPE', 'postgresql'),
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', '5432'),
    'database': os.getenv('DB_NAME', 'vaccination_db'),
    'user': os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD', '')
}

def get_connection_string():
    # Escape special characters in password
    password = quote_plus(DB_CONFIG['password'])
    return f"postgresql://{DB_CONFIG['user']}:{password}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
