CREATE TABLE IF NOT EXISTS categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    description VARCHAR(255)
);
CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(20) NOT NULL UNIQUE,
    price DECIMAL(10,2) NOT NULL CHECK(price >0),
    quantity INTEGER NOT NULL CHECK(quantity>0) DEFAULT 0,
    category_id INTEGER REFERENCES categories(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS suppliers (
    id SERIAL PRIMARY KEY,
    company_name VARCHAR(50) NOT NULL,
    contact_email VARCHAR(50) NOT NULL UNIQUE
);
INSERT INTO categories (name, description) 
VALUES ('elettronica', 'descrizione elettronica'), 
       ('giardini', 'descrizione giardino');