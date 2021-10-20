import os
from fastapi import Request,Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from api.exceptions.auth import credentials_exception

JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
JWT_ALGORITHM = os.environ.get('JWT_ALGORITHM')

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class AuthMiddleware:
    def __init__(self, app):
        self._app = app

    async def __call__(self, request:Request, call_next, token=Depends(oauth2_scheme)):
        try:
            print(token)
            payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
            print(payload)
            response = await call_next(request)
            return response
        except JWTError:
            raise credentials_exception
