import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv 

load_dotenv()

def create_table():
    conn = psycopg2.connect(
        dbname=os.environ.get("POSTGRES_DB"),
        user=os.environ.get("POSTGRES_USER"),
        password=os.environ.get("POSTGRES_PASSWORD"),
        host=os.environ.get("POSTGRES_HOST"),
        port=os.environ.get("POSTGRES_PORT")
    )
    cursor = conn.cursor()

    create_schema_query = """
    CREATE SCHEMA IF NOT EXISTS inventory;
    """
    cursor.execute(create_schema_query)
    
    set_schema_query = """
    SET search_path TO inventory;
    """
    cursor.execute(set_schema_query)
    
    create_table_query = """
    CREATE TABLE IF NOT EXISTS products (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        description TEXT,
        price DECIMAL(10, 2)
    );
    """
    cursor.execute(create_table_query)
    conn.commit()
    cursor.close()
    conn.close()

    print("Tabla 'products' creada exitosamente")

if __name__ == "__main__":
    create_table()
