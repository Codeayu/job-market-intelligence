from src.validation.validate_products import validate_products


products = [
    {
        "id": 1,
        "title": "Phone",
        "price": 100,
        "rating": 4,
        "category": "electronics"
    },
    {
        "id": -5,
        "title": "Bad Product",
        "price": -100,
        "rating": 20,
        "category": "electronics"
    },
    {
        "id": 2,
        "title": "Laptop",
        "price": 500,
        "rating": 4.5,
        "category": "electronics"
    }
]

valid, invalid = validate_products(products)

print("Valid:", len(valid))
print("Invalid:", len(invalid))