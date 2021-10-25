import enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Enum, Integer
from sqlalchemy import Column, String
from app.models.baseModel import BaseModel

class status(enum.Enum):
    open = 'open'
    close = 'close'
    cancelled = 'cancelled'

class ServiceUsedRecord(BaseModel):
    __tablename__='service_used_record'

    patient_id=Column(Integer,ForeignKey('patient.id'))
    patient = relationship('Patient')
    service_item_id = Column(Integer,ForeignKey('service_item.id'))
    service_item = relationship('ServiceItem')
    name = Column(String)
    quantity = Column(Integer)
    rate = Column(Integer)
    sub_total = Column(Integer)
    remark = Column(String)
    status = Column(Enum(status))