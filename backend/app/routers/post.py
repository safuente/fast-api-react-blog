import shutil
import string
import random

from fastapi import APIRouter, Depends, UploadFile, File
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


@router.get('/')
def get_all_posts(db: Session = Depends(get_db)):
    return post.get_all(db)


@router.delete('/{id}')
def delete_post(id: int, db: Session = Depends(get_db)):
    return post.delete(db, id)


@router.post('/image')
def upload_image(image: UploadFile = File(...)):
    letter = string.ascii_letters
    rand_str = ''.join(random.choice(letter) for i in range(6))
    new = f'_{rand_str}.'
    filename = new.join(image.filename.rsplit('.', 1))
    path = f'images/{filename}'

    with open(path, "w+b") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {
        'filename': path
    }
