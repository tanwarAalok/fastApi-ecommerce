# product id, product name, product category, product review, product cost
from pydantic import BaseModel
from enum import Enum


class CategoryProduct(str, Enum):
    ELECTRONICS = 'electronics'
    HOME = 'HOME'
    BEAUTY = 'BEAUTY'
    APPLIANCES = 'APPLIANCES'



class Product(BaseModel):
    productName: str
    productCategory: CategoryProduct
    productCost: float
    productImg: str
    productDescription: str
    sellerQuantity: int
    avgRating: int
