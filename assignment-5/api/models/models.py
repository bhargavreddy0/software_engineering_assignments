from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Sandwich(Base):
    __tablename__ = "sandwiches"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sandwich_name = Column(String(100), unique=True, nullable=False)
    price = Column(DECIMAL(6, 2), nullable=False)

    recipes = relationship("Recipe", back_populates="sandwich", cascade="all, delete-orphan")
    order_details = relationship("OrderDetail", back_populates="sandwich", cascade="all, delete-orphan")

class Resource(Base):
    __tablename__ = "resources"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    item = Column(String(100), unique=True, nullable=False)
    amount = Column(Integer, nullable=False)

    recipes = relationship("Recipe", back_populates="resource", cascade="all, delete-orphan")

class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"), nullable=False)
    resource_id = Column(Integer, ForeignKey("resources.id"), nullable=False)
    amount = Column(Integer, nullable=False)

    sandwich = relationship("Sandwich", back_populates="recipes")
    resource = relationship("Resource", back_populates="recipes")

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100), nullable=False)
    description = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    order_details = relationship("OrderDetail", back_populates="order", cascade="all, delete-orphan")

class OrderDetail(Base):
    __tablename__ = "order_details"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"), nullable=False)
    amount = Column(Integer, nullable=False)

    order = relationship("Order", back_populates="order_details")
    sandwich = relationship("Sandwich", back_populates="order_details")
