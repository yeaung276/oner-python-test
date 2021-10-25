from typing import Tuple
from fastapi import HTTPException,status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.session import Session

from app.models.baseModel import Role, User
from app.schemas.user import UserRegister
from app.services.common import CRUDService
from exceptions.auth import unauthorize_exception

from utils.hash import verify,create_token,hash

class AuthService:
    """auth services"""
    def __init__(self,db:Session,user:User):
        self.db = db
        self.user = user
        self.crud_service = CRUDService(db,user)

    def register(self,user:UserRegister)->User:
        try:
            new_user = User(**user.get_hashed())
            self.db.add(new_user)
            self.db.commit()
            self.db.refresh(new_user)
            return user
        except IntegrityError:
            raise HTTPException(status_code=404)

    def login(self,username,password) -> Tuple[str,User]:
        try:
            user = self.db.query(User).filter(User.username==username).first()
            if not verify(password,user.password_hash):
                raise unauthorize_exception
            token = create_token({'username': user.username, 'role': user.role})
        except:
            raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail= 'Cannot create credential'
            )
        return token,user
        
    def change_password(self,new_password:str,old_password:str):
        print(self.user)
        try:
            if not verify(old_password,self.user.password_hash):
                raise unauthorize_exception
            self.user.password_hash = hash(new_password)
        except:
            raise unauthorize_exception
            