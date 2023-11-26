
## User Model Structure

```python
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
    sellerId: List[str]=[]
    avgRating: int
```
