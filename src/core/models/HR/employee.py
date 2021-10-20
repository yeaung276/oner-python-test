import enum
from sqlalchemy import Column, String, Enum, Boolean, Integer,Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from core.models.baseModel import BaseModel

class MaritalStatus(enum.Enum):
    single = 'single'
    married = 'married'
    divorced = 'divorced'

class Status(enum.Enum):
    resigned = 'resigned'
    probation = 'probation'
    permanent = 'permanent'

class Employee(BaseModel):
    __tablename__='employee'

    id = Column(Integer, index=True, autoincrement=True, primary_key=True)
    name = Column(String)
    gender = Column(String)
    education = Column(String)
    marital_status = Column(Enum(MaritalStatus))
    number_of_children = Column(Integer)
    live_with_spouse_parent = Column(Boolean)
    phone = Column(String)
    emergency_phone = Column(String)
    date_of_birth = Column(Date)
    nrc_number = Column(String)
    bank_account_number = Column(String)
    address = Column(String)
    position_id = Column(Integer, ForeignKey('position.id'))
    department_id = Column(Integer, ForeignKey('department.id'))
    status = Column(Enum(Status))

    position = relationship('Position', uselist=False)
    department = relationship('Department', uselist=False)