from fastapi import Fastapi
from pydantic import BaseModel, Field
from schemas import Product, ProductCreate, ProductUpdate, Order, OrderCreate 
from database import products


class InfoAdd(BaseModel):
    name: str | int = Field(min_lenght=2, max_lenght=3, default=None)

app = FastAPI()

#@app.get("/info")
#def info():
    #return {"message": "info"}

#@app.post("/add/info")
#def add_info(body: InfoAdd):
    #return {"message": "success"}

@app.get("/")
def root():
    return {"message": "Cosmetics marketplace"}

@app.get("/products")
def get_products():
    return products 

@app.get("/products/{prod_id}")
def get_product_by_id(prod_id: int):
    for prod in products:
        if prod.id == prod_id:
            return prod
    return None 


@app.post("/products")
def create_product(product_data: ProductCreate):
    next_id = products[-1].id + 1
    product = Product(
        id = next_id,
        name = product_data.name,
        price = product_data.price,
        description = product_data.description
    )

products.append(product)

@app.path("/products/{prod_id}")
def update_product(prod_id: int, product_data: ProductUpdate):
    prod_ind = 0
    for prod in products:
        if prod.id == prod_id:
            product_to_update = prod
            prod_ind = products.index(prod)
        if prod_ind == -1:
            return {"error": "Value error, product not found"}
    updated_data = product_data.model_dump(exclude_unset=True)
    update_product = product_to_update | updated_data
    products[prod_ind] = update_product
