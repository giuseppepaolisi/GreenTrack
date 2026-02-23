from schema import BaseProductInput, BaseProductOutput
from models.products_model import ProductsModel

class ProductsController:
    
    @staticmethod
    def get_all_products(conn):
        products = ProductsModel.get_all_products(conn)
        return products
    
    @staticmethod
    def add_product(product : BaseProductInput, conn) -> BaseProductOutput:
        if not product.name or product.price is None or product.quantity is None or product.category_id is None:
            raise ValueError("All fields are required")
        new_product = ProductsModel.add_product(product, conn)
        if new_product:
            return BaseProductOutput(
                id=new_product[0],
                name=new_product[1],
                price=new_product[2],
                quantity=new_product[3],
                category_id=new_product[4]
            )
        return  # può tornare un errore