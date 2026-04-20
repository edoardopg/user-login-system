from database import get_connection
from fastapi import APIRouter
import bcrypt
from jose import jwt
from crud.users import Users
from pydantic import BaseModel
from datetime import datetime,timedelta
from utils.security import verify_password,hash_password

router = APIRouter()

SECRET_KEY = "long_secret_key_and_secure"
ALGORITHM = "HS256"

class LoginSchema(BaseModel):
    username: str
    password: str

class RegisterSchema(BaseModel):
    username: str
    email: str
    password: str

@router.post("/register")
def register(data: RegisterSchema):
    users = Users()
    if users.find_by_username(data.username):
        return {"error": "username already exists"}
    if users.find_by_email(data.email):
        return {"error": "email already exists"}
    hashed = hash_password(data.password)
    users.register(data.username,data.email,hashed)
    return {"message": "user registered successfully"}


@router.post("/login")
def login(data: LoginSchema):
    users = Users()
    user = users.find_by_username(data.username)
    if user is None:
        return {"error": "user not found"}
    if user[5] == 1:
        return {"error": "User is blocked, reset your password to unlock"}
    if not verify_password(data.password,user[3]):
        users.increment_attempts(data.username)
        user_updated = users.find_by_username(data.username)  # busca de nuevo
        if user_updated[4] >= 3:
            users.block_user(data.username)
            return {"error": "User blocked after 3 failed attempts"}
        return {"error": "Incorrect password"}
    users.reset_attempts(data.username)
    token = jwt.encode({"sub": data.username, "exp": datetime.utcnow() + timedelta(hours=8)},
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    return {"access_token": token}from database import get_connection
from fastapi import APIRouter
import bcrypt
from jose import jwt
from crud.users import Users
from pydantic import BaseModel
from datetime import datetime,timedelta
from utils.security import verify_password,hash_password

router = APIRouter()

SECRET_KEY = "long_secret_key_and_secure"
ALGORITHM = "HS256"

class LoginSchema(BaseModel):
    username: str
    password: str

class RegisterSchema(BaseModel):
    username: str
    email: str
    password: str

@router.post("/register")
def register(data: RegisterSchema):
    users = Users()
    if users.find_by_username(data.username):
        return {"error": "username already exists"}
    if users.find_by_email(data.email):
        return {"error": "email already exists"}
    hashed = hash_password(data.password)
    users.register(data.username,data.email,hashed)
    return {"message": "user registered successfully"}


@router.post("/login")
def login(data: LoginSchema):
    users = Users()
    user = users.find_by_username(data.username)
    if user is None:
        return {"error": "user not found"}
    if user[5] == 1:
        return {"error": "User is blocked, reset your password to unlock"}
    if not verify_password(data.password,user[3]):
        users.increment_attempts(data.username)
        user_updated = users.find_by_username(data.username)  # busca de nuevo
        if user_updated[4] >= 3:
            users.block_user(data.username)
            return {"error": "User blocked after 3 failed attempts"}
        return {"error": "Incorrect password"}
    users.reset_attempts(data.username)
    token = jwt.encode({"sub": data.username, "exp": datetime.utcnow() + timedelta(hours=8)},
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    return {"access_token": token}