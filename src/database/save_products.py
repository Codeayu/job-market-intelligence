import psycopg
from src.config.logger import logger


def save_products(connection, products):
    cursor = connection.cursor()

    insert_query = """
        INSERT INTO products
        (id, title, price, rating, category)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (id)
        DO UPDATE SET
            title = EXCLUDED.title,
            price = EXCLUDED.price,
            rating = EXCLUDED.rating,
            category = EXCLUDED.category
    """

    try:
        for product in products:
            cursor.execute(
                insert_query,
                (
                    product["id"],
                    product["title"],
                    product["price"],
                    product["rating"],
                    product["category"]
                )
            )

        connection.commit()

        logger.info("Successfully saved products")

        return True

    except psycopg.Error as e:
        connection.rollback()

        logger.error("Failed to save products: %s", e)

        return False

    finally:
        cursor.close()