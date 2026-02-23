

class ProductsModel:
    
    @staticmethod
    def add_product(product, conn):
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO products (name, price, quantity, category_id)
                VALUES (%s, %s, %s, %s)
                RETURNING id, name, price, quantity, category_id;
                """,
                (product.name, product.price, product.quantity, product.category_id)
            )
            new_product = cur.fetchone()
            conn.commit()
            return new_product
        
        return None
    
    @staticmethod
    def get_all_products(conn):
        with conn.cursor() as cur:
            cur.execute("SELECT id, name, price, quantity, category_id FROM products;")
            products = cur.fetchall()
            return products
        
        return []