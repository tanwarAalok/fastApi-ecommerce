
## User Model Structure

```python
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
```

## Review Model Structure

```python
class Review(BaseModel):
    userId: str
    rating: int
    comment: str
    createdAt: datetime
    updatedAt: datetime
```

## Product Model Structure

```python
class Product(BaseModel):
    productName: str
    productCategory: CategoryProduct
    productCost: float
    productImg: str
    productDescription: str
    sellerQuantity: int
    avgRating: int
```
