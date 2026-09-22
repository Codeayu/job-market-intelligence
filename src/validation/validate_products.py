from src.validation.schemas import Product
from pydantic import ValidationError
from src.config.logger import logger

def validate_products(products):

    valid_products = []
    invalid_products = []

    for product in products:

        try:
            validate_product = Product(**product)
            valid_products.append(validate_product.model_dump())


        except ValidationError as e:
            invalid_products.append(product)
            logger.warning(
            "Product %s failed validation: %s",
             product.get("id"),
                e
)
            

    return valid_products, invalid_products