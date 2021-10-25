import os
from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import jwt, JWTError

SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
ALGORITHM = os.environ.get('JWT_ALGORITHM')

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def hash(password):
    return pwd_context.hash(password)

def verify(plain_passw, hash_passw):
    return pwd_context.verify(plain_passw, hash_passw)

def create_token(data: dict):
    JWT_EXPIRY_MINUTE = os.environ.get('JWT_EXPIRY_MINUTE')
    expires_delta = timedelta(minutes=int(JWT_EXPIRY_MINUTE))
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({'exp': expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token