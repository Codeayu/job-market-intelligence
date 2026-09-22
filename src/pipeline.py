from src.ingestion.fetch_products import fetch_products
from src.transformation.clean_products import clean_products
from src.database.connection import get_connection
from src.database.save_products import save_products
from src.validation.validate_products import validate_products
from src.config.logger import logger


def run_pipeline():
    #fetching
    products = fetch_products()
    logger.info("Fetched %d products", len(products))

    #Cleaning
    cleaned_products = clean_products(products)
    logger.info("Cleaned %d products", len(cleaned_products))


    #Validation Error
    valid_products, invalid_products = validate_products(cleaned_products)
    logger.info("Valid products: %d", len(valid_products))
    logger.warning("Invalid products: %d", len(invalid_products))  


    connection = None
    #Database connection
    try:
        # Database connection
        connection = get_connection()

        if connection is None:
            logger.error("Pipeline stopped: database connection failed")
            return

        # Saving
        saved = save_products(connection, valid_products)

        if saved:
            logger.info("Products saved successfully")
        else:
            logger.warning("Products were not saved")

    finally:
        if connection:
            connection.close()







if __name__ == "__main__":
    run_pipeline()