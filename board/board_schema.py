from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class NewPost(BaseModel):
    writer: str
    title: str
    content: Optional[str] = None # 내용은 없어도 됌

class Post_List(BaseModel):
    no: int
    writer: str
    title: str
    date: datetime

class Post(BaseModel):
    no: int
    writer: str
    title: str
    content: Optional[str] = None #없을 수도 있으니 Optional로
    date: datetime

class Update_Post(BaseModel):
    no: int
    title: str 
    content: Optional[str] = None #없을 수도 있으니 Optional로

class Update_Post(BaseModel):
    no: int
    title: str 
    content: Optional[str] = None #없을 수도 있으니 Optional로