import psycopg
from src.config.logger import logger

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

        logger.info("Database connected successfully")

        return connection

    except psycopg.Error as e:
        logger.error("Database connection failed: %s", e)

        return None