def save_products(connection, products):
    cursor = connection.cursor()

    insert_query = """

    INSERT INTO products
    (id, title, price, rating, category)
    VALUES(%s,%s,%s,%s,%s) 
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
        cursor.close()
        return True

    except Exception as e:
        connection.rollback()
        print("❌ Failed to save products:", e)
        return False

    finally:
        cursor.close()