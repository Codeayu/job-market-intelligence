from src.ingestion.fetch_products import fetch_products
from src.transformation.clean_products import clean_products
from src.database.connection import get_connection
from src.database.save_products import save_products


def run_pipeline():
    #fetching
    products = fetch_products()
    print(f"📥 Fetched {len(products)} products")

    #Cleaning
    cleaned_products = clean_products(products)
    print(f"🧹 Cleaned {len(cleaned_products)} products")

    #Database connection
    try:
        # Database connection
        connection = get_connection()

        if connection is None:
            print("❌ Pipeline stopped: database connection failed.")
            return

        # Saving
        saved = save_products(connection, cleaned_products)

        if saved:
            print("💾 Products saved successfully!")
        else:
            print("⚠️ Products were not saved.")

    finally:
        if connection:
            connection.close()







if __name__ == "__main__":
    run_pipeline()