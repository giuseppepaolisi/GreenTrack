from schema import BaseProductInput, BaseProductOutput

class ProductsController:
    
    @staticmethod
    def get_all_products(conn):
        sql = """SELECT * FROM products;"""
        with conn.cursor() as cur:
            cur.execute(sql)
            products = cur.fetchall()
            
            return products
        return []
    
    @staticmethod
    def add_product(product : BaseProductInput, conn) -> BaseProductOutput:
        sql = """INSERT INTO products (name, price, quantity, category_id) VALUES(%s, %s, %s, %s);"""
        new_product = None
        with conn.cursor() as cur:
            cur.execute(sql, (product.name, product.price, product.quantity, product.category_id))
            new_product = cur.fetchone()
            conn.commit()
            
        return new_product