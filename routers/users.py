from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from jose import jwt
from crud.users import Users
from pydantic import BaseModel
from datetime import datetime,timedelta
from utils.security import verify_password,hash_password,generate_reset_token,get_expiration_time
from utils.email import send_reset_email

router = APIRouter()

SECRET_KEY = "long_secret_key_and_secure"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

class RegisterSchema(BaseModel):
    username: str
    email: str
    password: str

class ForgotPasswordSchema(BaseModel):
    email: str

class ResetPasswordSchema(BaseModel):
    new_password:str
    token:str

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
def login(data: OAuth2PasswordRequestForm = Depends()):
    users = Users()
    user = users.find_by_username(data.username)
    if user is None:
        return {"error": "user not found"}
    if user[5] == 1:
        return {"error": "User is blocked, reset your password to unlock"}
    if not verify_password(data.password, user[3]):
        users.increment_attempts(data.username)
        user_updated = users.find_by_username(data.username)
        if user_updated[4] >= 3:
            users.block_user(data.username)
            return {"error": "User blocked after 3 failed attempts"}
        return {"error": "Incorrect password"}
    users.reset_attempts(data.username)
    token = jwt.encode(
        {"sub": data.username, "exp": datetime.utcnow() + timedelta(hours=8)},
        SECRET_KEY,
        algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}

@router.post("/forgot-password")
def forgot_password(data: ForgotPasswordSchema):
    users = Users()
    if not users.find_by_email(data.email):
        return {"error": "email not found"}
    token = generate_reset_token()
    users.save_reset_token(data.email,token,get_expiration_time())
    send_reset_email(data.email,token)
    return {"message": "email sent, check your inbox"}

@router.post("/reset-password")
def reset_password(data: ResetPasswordSchema):
    users = Users()
    user = users.find_by_token(data.token)
    if not user:
        return {"error":"token not found"}
    if datetime.now() > datetime.fromisoformat(str(user[7])):
        return {"error":"Link expired"}
    hashed = hash_password(data.new_password)
    users.update_password(user[2],hashed)
    users.unblock_user(user[1])
    users.reset_attempts(user[1])
    return {"message":"update password successfully"}

@router.delete("/delete-account")
def delete_account(usuario=Depends(verify_token)):
    users = Users()
    username = usuario["sub"]  # el username está dentro del token
    users.delete_account(username)
    return {"message": "Account deleted successfully"}
