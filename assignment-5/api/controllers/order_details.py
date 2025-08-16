from fastapi import Response, status
from sqlalchemy.orm import Session
from ..models import models
from ..models import schemas

def create(db: Session, order_detail: schemas.OrderDetailCreate):
    db_obj = models.OrderDetail(**order_detail.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def read_all(db: Session):
    return db.query(models.OrderDetail).all()

def read_one(db: Session, order_detail_id: int):
    return db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()

def update(db: Session, order_detail_id: int, order_detail: schemas.OrderDetailUpdate):
    q = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id)
    update_data = order_detail.dict(exclude_unset=True)
    q.update(update_data, synchronize_session=False)
    db.commit()
    return q.first()

def delete(db: Session, order_detail_id: int):
    q = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id)
    q.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
