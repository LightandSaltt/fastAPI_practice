from fastapi import FastAPI

import models
from databae import engine
models.Base.metadata.create_all(bind=engine)

from user import user_router
from board import board_router

app = FastAPI()

#서버 실행
#/usr/bin/python3 /Users/apple/Library/Python/3.9/bin/uvicorn main:app --reload

#DB 확인
#sqlite3 fastapi.db
#.database

#테이블 확인
#.tables
#SELECT sql FROM sqlite_master WHERE tbl_name='{테이블명}'
#SELECT * FROM Board; <- 모든 컨텐츠 보기

app.include_router(user_router.app, tags=["user"])
app.include_router(board_router.app, tags=["board"])

@app.get("/")
def hello():
    return {"Hello : World!"}

#curl -X POST "http://127.0.0.1:8000/board/create" -H "accept: application/json" -H "Content-Type: application/json" -d '{"writer": "Hanni", "title": "NewJeans", "content": "OMG"}'
