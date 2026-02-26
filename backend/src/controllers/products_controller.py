from schema import BaseProductInput, BaseProductOutput
from models.products_model import ProductsModel
"""
    La differenza è nel tipo di dati che stai unpacking:

*p → unpacking di sequenze (liste, tuple): distribuisce gli elementi come argomenti posizionali
**p → unpacking di dizionari: distribuisce le coppie chiave-valore come argomenti con nome (keyword arguments)

"""

class ProductsController:
    
    @staticmethod
    def get_all_products(conn):
        products = ProductsModel.get_all_products(conn)
        return [BaseProductOutput(**p) for p in products]
    
    @staticmethod
    def add_product(product : BaseProductInput, conn) -> BaseProductOutput:
        if not product.name or product.price is None or product.quantity is None or product.category_id is None:
            raise ValueError("All fields are required")
        res = ProductsModel.add_product(product, conn)
        return BaseProductOutput(**res)
    
    @staticmethod
    def delete_product(id: int, conn):
        deleted = ProductsModel.delete_product(id, conn)
        if not deleted:
            {"message": "prodotto non trovato"}
        return {"message": "Eliminato"}