
from psycopg2.extras import RealDictCursor

class ProductsModel:
    
    @staticmethod
    def add_product(product, conn):
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
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
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM products;")
            products = cur.fetchall()
            return products
        
        return []
    
    @staticmethod
    def delete_product(id, conn):
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("DELETE FROM products WHERE id = %s;", (id,))
            conn.commit()
            return True
        return False