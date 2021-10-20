from enum import auto
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy import Column
from core.models.baseModel import BaseModel

class InvestigationCategory(BaseModel):
    __tablename__='investigation_category'
    id=Column(Integer,index=True,primary_key=True,autoincrement=True)
    name=Column(String)