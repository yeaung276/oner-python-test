from datetime import datetime
from fastapi.param_functions import Depends
from sqlalchemy.ext.declarative import AbstractConcreteBase
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import DateTime, Integer, String
from sqlalchemy.orm import relationship, Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__='user'

    id = Column(Integer, index=True, autoincrement=True, primary_key=True)
    fullname = Column(String)
    username = Column(String, unique=True)
    password_hash = Column(String)
    role_id = Column(Integer, ForeignKey('role.id'))

    role = relationship('Role', backref='user')

class Role(Base):
    __tablename__='role'

    id = Column(Integer, index=True, autoincrement=True, primary_key=True)
    name = Column(String)

class BaseModel(AbstractConcreteBase, Base):
    created_time = Column(DateTime, default=datetime.utcnow())
    updated_time = Column(DateTime, default=datetime.utcnow())
    @declared_attr
    def created_user_id(cls):
        return Column(Integer, ForeignKey('user.id'), default=0)
    @declared_attr
    def updated_user_id(cls):
        return Column(Integer, ForeignKey('user.id'), default=0)
    @declared_attr
    def created_user(cls):
        return relationship('User', primaryjoin=lambda: User.id==cls.created_user_id)
    @declared_attr
    def updated_user(cls):
        return relationship('User', primaryjoin=lambda: User.id==cls.updated_user_id)

    def set_stamp(self, user:User):
        self.created_time = datetime.utcnow()
        self.created_user_id = user.id
        self.updated_time = datetime.utcnow()
        self.updated_user_id = user.id

    def update_stamp(self, user:User):
        self.updated_time = datetime.utcnow()
        self.updated_user_id = user.id

    def add(self,user:User,db:Session):
        """default add bahaviour"""
        self.set_stamp(user)
        db.add(self)
        db.commit()
        db.refresh(self)
        return self

    def update(self,data:dict,user:User,db:Session):
        """default update behaviour"""
        for key,value in data.items():
            setattr(self,key,value)
        self.update_stamp(user)
        db.commit()
        db.refresh(self)
        return self