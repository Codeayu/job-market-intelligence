import requests as req


URL = "https://dummyjson.com/products"


def fetch_products():
    try:
        response = req.get(URL)

        response.raise_for_status()

        data = response.json()

        products = data["products"]

        return products

    except req.exceptions.RequestException as e:
        print("❌ Failed to fetch products:", e)

        return []