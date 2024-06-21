from sqlalchemy.orm import Session
from databae import get_db

from user import user_schema
from user import user_crud

from fastapi import APIRouter, Depends, HTTPException, status

app = APIRouter(
    prefix="/user",
)

@app.post(path="/signup")
async def signup(new_user: user_schema.NewUserForm, db: Session= Depends(get_db)):
    #회원 존재 여부 확인 
    user = user_crud.get_user(new_user.email, db)

    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists.")
    
    #회원가입
    user_crud.create_user(new_user, db)

    return HTTPException(status_code=status.HTTP_200_OK, detail= "Sign up successful")



