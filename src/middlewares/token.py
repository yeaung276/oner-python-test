from datetime import datetime
import os
from fastapi.param_functions import Depends
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from exceptions.auth import credentials_exception

JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
JWT_ALGORITHM = os.environ.get('JWT_ALGORITHM')

# unused
class TokenExpiry(BaseHTTPMiddleware):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    async def dispatch(request: Request, call_next,):
        if "Authorization" not in request.headers:
            raise credentials_exception
        auth = request.headers["Authorization"]
        try:
            _, credentials = auth.split()
            payload = jwt.decode(credentials, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
            if datetime.utcnow() > payload.get('exp'):
                raise credentials_exception
            response = await call_next(request)
            return response
        except JWTError:
            raise credentials_exception

