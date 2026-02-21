from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    id: int
    name: str
    price: float
    description: Optional[str] = None


class User(BaseModel):
    id: int
    username: str
    password: str


class CartItem(BaseModel):
    user_id: int
    item_id: int
    quantity: int
