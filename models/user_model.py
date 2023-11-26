from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel, EmailStr


class UserRoles(str, Enum):
    SELLER = 'seller'
    BUYER = 'buyer'


class SellerProductInfo(BaseModel):
    product_id: str
    stock: int


class BaseUser(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: UserRoles
    createdAt: datetime
    updatedAt: datetime


class UserBuyer(BaseUser):
    review_ids: List[str] = []


class UserSeller(BaseUser):
    products: List[SellerProductInfo] = []


class User(BaseUser):
    @property
    def __actual_class__(self):
        if self.role == 'seller':
            return UserSeller
        elif self.role == 'buyer':
            return UserBuyer
        return User
