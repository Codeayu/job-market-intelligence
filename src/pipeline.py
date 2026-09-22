from src.ingestion.fetch_products import fetch_products
from src.transformation.clean_products import clean_products
from src.database.connection import get_connection
from src.database.save_products import save_products
from src.validation.validate_products import validate_products
from src.validation.quality_checks import check_duplicate_ids
from src.config.logger import logger


def run_pipeline():
    metrics = {
        "fetched" : 0,
        "valid" : 0,
        "invalid" : 0,
        "saved" : 0

    }
    #fetching
    products = fetch_products()
    if not products:
        logger.warning("No products fetched. Pipeline stopped.")
        return metrics
    metrics["fetched"] = len(products)
    logger.info("Fetched %d products", len(products))

    #Cleaning
    cleaned_products = clean_products(products)
    logger.info("Cleaned %d products", len(cleaned_products))


    #Validation Error
    valid_products, invalid_products = validate_products(cleaned_products)
    metrics["valid"]=len(valid_products)
    metrics["invalid"] = len(invalid_products)
    logger.info("Valid products: %d", metrics["valid"])
    logger.warning("Invalid products: %d", metrics["invalid"])  

    #Quality Checks
    quality = check_duplicate_ids(valid_products)
    if quality:
        logger.info("Data quality check passed: all product IDs are unique")
    else:
        logger.warning("Data quality check failed: duplicate product IDs found")


    connection = None
    #Database connection
    try:
        # Database connection
        connection = get_connection()

        if connection is None:
            logger.error("Pipeline stopped: database connection failed")
            return metrics

        # Saving
        saved = save_products(connection, valid_products)
        metrics["saved"] = saved

        if saved:
            logger.info("Successfully saved %d products",saved)
        else:
            logger.warning("Products were not saved")

        logger.info(
        "Pipeline completed: fetched=%d, valid=%d, invalid=%d, saved=%d",
        metrics["fetched"],
        metrics["valid"],
        metrics["invalid"],
        metrics["saved"]
        )
    finally:
        if connection:
            connection.close()








if __name__ == "__main__":
    run_pipeline()