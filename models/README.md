
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

