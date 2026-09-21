def clean_products(products):
    cleaned_products = []

    for product in products:
        cleaned = {
            "id": product["id"],
            "title": product["title"].strip(),
            "price": product["price"],
            "rating": product.get("rating", 0),
            "category": product["category"].strip().lower()
        }

        cleaned_products.append(cleaned)

    return cleaned_products