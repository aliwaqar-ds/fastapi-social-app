from typing import Optional

from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models, schemas, utils
from .database import engine, get_db
from .routers import post,user,auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


while True:
    try:
        conn = psycopg2.connect(host='localhost',database='fastapi',user='postgres',
        password='Pakistan123',cursor_factory= RealDictCursor)
        cursor = conn.cursor()
        print("Database connection successful!")
        break
    except Exception as error:
        print("Connection to database failed")
        print("Error", error)
        time.sleep(2)


my_post = [{"title" : 'This is my title', "content" : "This is the content of post 1 ", "id" : 1},
           {"title" : "my favourite foods", "content" : "these are my fav foods", "id" : 2}]

def find_post(id):
    for p in my_post:
        if p["id"] == id:
            return p
        
def find_index_post(id):
    for i,p in enumerate(my_post):
        if p['id'] == id:
            return i


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"message": "welcome to my api"}


