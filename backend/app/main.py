from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import models
from database import engine
from routers import post
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.include_router(post.router)


models.Base.metadata.create_all(engine)

app.mount('/images', StaticFiles(directory='images'), name='images')

origins = [
    "*"
]

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=['*'],
                   allow_headers=['*'])
