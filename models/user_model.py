from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel, EmailStr

class UserRoles(str, Enum):
    SELLER = 'seller'
    BUYER = 'buyer'

class User(BaseModel):
    name: str
    role: UserRoles
    email: EmailStr
    password: str
    review_ids: List[str] = []
    createdAt: datetime
    updatedAt: datetime

