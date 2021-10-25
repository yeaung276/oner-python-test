from datetime import datetime
import os
from typing import List
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import jwt, JWTError

from app.models import User
from database import get_db
from exceptions.auth import credentials_exception, unauthorize_exception

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
JWT_ALGORITHM = os.environ.get('JWT_ALGORITHM')

def get_user(access_roles:List[str]):
    async def get_current_user(token:str=Depends(oauth2_scheme), db:Session=Depends(get_db)):
        try:
            payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
            user = db.query(User).filter(User.username==payload['username']).first()
            if user.role not in access_roles:
                raise unauthorize_exception
            if datetime.utcnow() > datetime.fromtimestamp(payload.get('exp')):
                raise unauthorize_exception
            return user
        except JWTError:
            raise credentials_exception

    return get_current_user