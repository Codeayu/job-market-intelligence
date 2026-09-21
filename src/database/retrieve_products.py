from src.database.connection import get_connection

def retrieve_products():

    connection = get_connection()

    if connection is None:
        print("error")
        return 


    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT *
            FROM products
            ORDER BY id;
        """)

        products = cursor.fetchall()

        print(f"📦 Total products: {len(products)}")

        for product in products:
            print(product)

    except Exception as e:
        print("❌ Failed to retrieve products:", e)

    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    retrieve_products()