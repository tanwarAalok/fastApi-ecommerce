# product id, product name, product category, product review, product cost
from pydantic import BaseModel
from enum import Enum
from typing import List


class CategoryProduct(str, Enum):
    ELECTRONICS = 'electronics'
    HOME = 'home'
    BEAUTY = 'beauty'
    APPLIANCES = 'appliances'


class Product(BaseModel):
    productName: str
    productCategory: CategoryProduct
    productCost: float
    productImg: str
    productDescription: str
    sellerId: List[str] = []
    avgRating: int
