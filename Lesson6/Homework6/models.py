from decimal import Decimal
from datetime import date
from pydantic import BaseModel, Field, EmailStr


class UserIn(BaseModel):
    firstname: str = Field(min_length=2, max_length=35)
    lastname: str = Field(min_length=2, max_length=80)
    email: EmailStr = Field(max_length=128)
    password: str = Field(min_length=8, max_length=128)


class User(BaseModel):
    id: int
    firstname: str = Field(min_length=2, max_length=35)
    lastname: str = Field(min_length=2, max_length=80)
    email: EmailStr = Field(max_length=128)
    password_hash: str


class ItemIn(BaseModel):
    title: str = Field(min_length=3, max_length=128)
    description: str = Field(min_length=3, max_length=512)
    price: Decimal = Field(gt=0, le=1_000_000)


class Item(ItemIn):
    id: int


class OrderIn(BaseModel, use_enum_values=True):
    user_id: int = Field(gt=0)
    item_id: int = Field(gt=0)
    date: date
    status: str = Field(min_length=2, max_length=64)


class Order(OrderIn):
    id: int
