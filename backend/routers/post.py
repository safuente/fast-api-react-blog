from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas.post import PostBase
from services import post

router = APIRouter(
    prefix='/post',
    tags=['post']
)

@router.post('/')
def create_post(request: PostBase, db: Session = Depends(get_db)):
    return post.create(db, request)
