import bcrypt
import secrets
from datetime import datetime,timedelta

def hash_password(password):
    hashed = bcrypt.hashpw(password.encode("utf-8"),bcrypt.gensalt()).decode("utf-8")
    return hashed
def verify_password(password,hashed):
    return bcrypt.checkpw(password.encode("utf-8"),hashed.encode("utf-8"))
def generate_reset_token():
    return secrets.token_urlsafe(32)
def get_expiration_time():
    return datetime.now() + timedelta(minutes=30)