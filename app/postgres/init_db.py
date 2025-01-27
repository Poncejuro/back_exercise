import psycopg2
from psycopg2 import sql
import os

def create_table():
    # Conexión a la base de datos PostgreSQL
    conn = psycopg2.connect(
        dbname=os.environ.get("POSTGRES_DB", "inventory"),
        user=os.environ.get("POSTGRES_USER", "admin"),
        password=os.environ.get("POSTGRES_PASSWORD", "abc123"),
        host=os.environ.get("POSTGRES_HOST", "localhost"),
        port=os.environ.get("POSTGRES_PORT", 5432)
    )
    cursor = conn.cursor()

    # Crear la tabla si no existe
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
