from sqlalchemy.sql.sqltypes import Integer
from sqlalchemy import Column, String
from core.models.baseModel import BaseModel


class Position(BaseModel):
    __tablename__='position'

    id = Column(Integer, index=True, autoincrement=True, primary_key=True)
    name = Column(String)
    description = Column(String)