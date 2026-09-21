CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    title VARCHAR(255),
    price NUMERIC(10, 2),
    rating NUMERIC(3, 2),
    category VARCHAR(100)
);