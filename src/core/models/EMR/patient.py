from sqlalchemy.sql.sqltypes import Boolean, Date, Integer
from sqlalchemy import Column, String
from core.models.baseModel import BaseModel


class Patient(BaseModel):
    __tablename__='patient'

    id = Column(Integer, index=True, autoincrement=True, primary_key=True)
    name = Column(String)
    gender = Column(String)
    date_of_birth = Column(Date)
    age = Column(Integer)
    address = Column(String)
    phone = Column(String)
    blood_group = Column(String)