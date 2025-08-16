from fastapi import Response, status
from sqlalchemy.orm import Session
from ..models import models
from ..models import schemas

def create(db: Session, order: schemas.OrderCreate):
    db_obj = models.Order(**order.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def read_all(db: Session):
    return db.query(models.Order).all()

def read_one(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.id == order_id).first()

def update(db: Session, order_id: int, order: schemas.OrderUpdate):
    q = db.query(models.Order).filter(models.Order.id == order_id)
    update_data = order.dict(exclude_unset=True)
    q.update(update_data, synchronize_session=False)
    db.commit()
    return q.first()

def delete(db: Session, order_id: int):
    q = db.query(models.Order).filter(models.Order.id == order_id)
    q.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
