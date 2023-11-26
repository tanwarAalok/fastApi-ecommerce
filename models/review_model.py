from datetime import datetime

from pydantic import BaseModel


class Review(BaseModel):
    userId: str
    rating: int
    comment: str
    createdAt: datetime
    updatedAt: datetime