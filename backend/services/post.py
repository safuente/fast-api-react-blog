from fastapi import HTTPException
from models import DbPost
from schemas.post import PostBase
from sqlalchemy.orm.session import Session
import datetime


def create(db: Session, request: PostBase):
    new_post = DbPost(
        image_url=request.image_url,
        title=request.title,
        content=request.content,
        creator=request.creator,
        timestamp=datetime.datetime.now()
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get_all(db: Session):
    posts = db.query(DbPost).all()
    return posts


def delete(db: Session, id: int):
    post = db.query(DbPost).filter(DbPost.id == id).first()
    if not post:
        raise HTTPException(status_code=404, detail=f"Post id {id} not found")
    db.delete(post)
    db.commit()
    return f"Post id {id} deleted"
