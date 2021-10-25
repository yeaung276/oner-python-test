from fastapi import APIRouter,Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.models.baseModel import Role

from app.services.auth import AuthService
from app.models import User
from app.schemas.user import ChangePassword, CredentialReturn, Login, UserRegister
from dependencies.auth import get_user
from database import get_db


auth = APIRouter(
    tags=['auth']
)

@auth.post('/register')
async def register(user:UserRegister, db:Session=Depends(get_db)):
    auth = AuthService(db,None)
    return auth.register(user)

@auth.post('/login')
async def login(login:Login, db:Session=Depends(get_db)):
    auth = AuthService(db,None)
    token,user = auth.login(login.username,login.password)
    return CredentialReturn(username=login.username,role=user.role,token=token)

@auth.post('/change_password')
async def changePassword(payload:ChangePassword, db:Session=Depends(get_db),user:User=Depends(get_user(['admin']))):
    auth = AuthService(db,user)
    auth.change_password(payload.new_password,payload.old_password)
    return {'message': 'done'}

@auth.post('/token')
async def token(form_data: OAuth2PasswordRequestForm = Depends(),db:Session=Depends(get_db)):
    auth = AuthService(db,None)
    token,_ = auth.login(form_data.username,form_data.password)
    return {
        'access_token': token,
        'token_type': 'bearer'
    }