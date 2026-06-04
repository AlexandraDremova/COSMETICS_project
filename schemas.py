from pydantic import FastAPI
from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    name: str = Field(min_lenght=2, max_lenght=80)
    category: str = Field(min_lenght=2, max_lenght=40)
    price: float = Field(gt=1)
    description: str = Field(min_lenght=5, max_lenght=300)

class ProductUpdate(BaseModel):
    name: str | None = Field(default=None, min_lenght=2, max_lenght=80)
    category: str | None = Field(default=None, min_lenght=2, max_lenght=40)
    price: float | None = Field(default=None, gt=1)
    description: str | None = Field(default=None, min_lenght=5, max_lenght=300)

class Product(ProductCreate):
    id: int

class OrderCreate(BaseModel):
    product_id: int
    customer_name: str = Field(min_lenght=2, max_lenght=60)
    type_of_cosmetics: str = Field(min_lenght=2, max_lenght=60)
    quantity: int = Field(gt=0, le=10)

class Order(OrderCreate):
    id: int
    total_price: float 
    
