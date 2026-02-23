from fastapi import routing, Depends, status
from core.database import db_manager
from controllers.products_controller import ProductsController
from schema import BaseProductInput, BaseProductOutput

router = routing.APIRouter(prefix="/api/products")

@router.get("/")
def get_products(conn = Depends(db_manager.get_conn)):
    return {"products": ProductsController.get_all_products(conn)}

@router.post("/", response_model=BaseProductOutput, status_code=status.HTTP_201_CREATED)
def add_product(product: BaseProductInput, conn = Depends(db_manager.get_conn)) -> BaseProductOutput:
    new_product = ProductsController.add_product(product, conn)
    return new_product

# regex