from enum import auto
from sqlalchemy import Column, String, Enum, Boolean, Integer,Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from core.models.baseModel import BaseModel


class Doctor(BaseModel):
    __tablename__ = 'doctor'
    id = Column(Integer, index=True, autoincrement=True, primary_key=True)
    employee_id = Column(Integer, ForeignKey('employee.id'))
    employee = relationship('Employee', uselist=False)
    schedule = Column(String)
    opd_charge_id = Column(Integer, ForeignKey('service_item.id'))
    opd_charge = relationship('ServiceItem',backref='doctor')
    ipd_charge_id = Column(Integer, ForeignKey('service_item.id'))
    ipd_charge = relationship('ServiceItem', uselist=False)