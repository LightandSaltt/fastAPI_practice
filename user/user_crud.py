from sqlalchemy.orm import Session

from models import User
from user.user_schema import NewUserForm

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user(email: str, db: Session):
    return db.query(User).filter(User.email == email).first()

def create_user(new_user: NewUserForm, db: Session):
    user = User(
    name=new_user.name,  # 또는 User 모델에 이미 있는 필드를 사용하여 수정
    email=new_user.email,
    hashed_pw=pwd_context.hash(new_user.password)
)
    db.add(user)
    db.commit()

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)