import requests as req
from src.config.logger import logger


URL = "https://dummyjson.com/products"


def fetch_products():
    try:
        response = req.get(URL)

        response.raise_for_status()

        data = response.json()

        products = data["products"]
        #logger.info("Fetched %d products", len(products))

        return products

    except req.exceptions.RequestException as e:
        logger.error("Unable to fetch products: %s", e)

        return []