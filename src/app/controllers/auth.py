from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sqlalchemy.exc import DBAPIError, IntegrityError

from core.models import get_db,Role,User
from core.schemas.user import ChangePassword, CredentialReturn, Login, UserRegister
from api.exceptions.auth import unauthorize_exception
from utils.auth import check_auth
from utils.hash import create_token

auth = APIRouter(
    tags=['auth']
)

@auth.post('/register')
async def register(user:UserRegister, db:Session=Depends(get_db)):
    try:
        if db.query(Role).get(user.role_id)==None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='role not found')
        new_user = User(**user.get_hashed())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except IntegrityError:
        raise HTTPException(status_code=404)
    return 'done'

@auth.post('/login')
async def login(login:Login, db:Session=Depends(get_db)):
    try:
        user = db.query(User).filter(User.username==login.username).first()
        if not user.verify(login.password):
            raise unauthorize_exception
    except:
        raise unauthorize_exception
    token = create_token({'username': user.username, 'role': user.role.name})
    response = CredentialReturn(username=user.username, role=user.role.name, token=token)
    return response

@auth.post('/change_password')
async def changePassword(payload:ChangePassword, db:Session=Depends(get_db),user:User=Depends(check_auth(['admin']))):
    if not user.verify(payload.old_password):
        raise unauthorize_exception  
    user.change_password(payload.new_password,db)
    return {'message': 'done'}

@auth.post('/token')
async def token(form_data: OAuth2PasswordRequestForm = Depends(),db:Session=Depends(get_db)):
    try:
        user = db.query(User).filter(User.username==form_data.username).first()
        if not user.verify(form_data.password):
            raise unauthorize_exception
    except:
        raise unauthorize_exception
    token = create_token({'username': user.username, 'role': user.role.name})
    response = {"access_token": token, "token_type": "bearer"}
    return response