from __future__ import annotations
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class SandwichBase(BaseModel):
    sandwich_name: str
    price: float

class SandwichCreate(SandwichBase):
    pass

class SandwichUpdate(BaseModel):
    sandwich_name: Optional[str] = None
    price: Optional[float] = None

class Sandwich(SandwichBase):
    id: int
    class Config:
        orm_mode = True


class OrderDetailBase(BaseModel):
    amount: int
    sandwich_id: int

class OrderDetailCreate(OrderDetailBase):
    order_id: Optional[int] = None

class OrderDetailUpdate(BaseModel):
    amount: Optional[int] = None
    sandwich_id: Optional[int] = None

class OrderDetail(OrderDetailBase):
    id: int
    order_id: int
    sandwich: Optional["Sandwich"] = None
    class Config:
        orm_mode = True


class OrderBase(BaseModel):
    customer_name: str
    description: Optional[str] = None

class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    description: Optional[str] = None

class Order(OrderBase):
    id: int
    created_at: datetime
    order_details: List[OrderDetail] = []
    class Config:
        orm_mode = True

class ResourceBase(BaseModel):
    item: str
    amount: int

class ResourceCreate(ResourceBase):
    pass

class ResourceUpdate(BaseModel):
    item: Optional[str] = None
    amount: Optional[int] = None

class Resource(ResourceBase):
    id: int
    class Config:
        orm_mode = True


class RecipeBase(BaseModel):
    amount: int
    sandwich_id: int
    resource_id: int

class RecipeCreate(RecipeBase):
    pass

class RecipeUpdate(BaseModel):
    amount: Optional[int] = None
    sandwich_id: Optional[int] = None
    resource_id: Optional[int] = None

class Recipe(RecipeBase):
    id: int
    class Config:
        orm_mode = True
