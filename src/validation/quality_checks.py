from src.config.logger import logger


def check_duplicate_ids(products):
    product_ids = []

    for product in products:
        product_ids.append(product["id"])

    unique_ids = set(product_ids)

    if len(unique_ids) == len(product_ids):
        
        return True

    return False