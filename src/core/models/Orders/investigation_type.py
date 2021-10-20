from enum import auto
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy import Column
from core.models.baseModel import BaseModel

class InvestigationType(BaseModel):
    __tablename__='investigation_type'
    id=Column(Integer, index=True, autoincrement=True,primary_key=True)
    name=Column(String)