import psycopg

from src.config.settings import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD
)


def get_connection():
    try:
        connection = psycopg.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )

        #print("✅ Database connected successfully!")

        return connection

    except psycopg.Error as e:
        print("❌ Database connection failed!")
        print(e)

        return None