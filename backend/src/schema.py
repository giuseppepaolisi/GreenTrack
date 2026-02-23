from pydantic import BaseModel

class BaseProduct(BaseModel):
    name: str
    price: float
    quantity: int
    category_id: int

class BaseProductInput(BaseProduct):
    pass

class BaseProductOutput(BaseProduct):
    id: int