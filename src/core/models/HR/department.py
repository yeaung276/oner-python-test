from sqlalchemy.sql.sqltypes import Integer
from sqlalchemy import Column, String
from core.models.baseModel import BaseModel


class Department(BaseModel):
    __tablename__='department'

    id = Column(Integer, index=True, autoincrement=True, primary_key=True)
    name = Column(String)
    description = Column(String)