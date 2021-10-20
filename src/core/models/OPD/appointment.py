import enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime, Enum, Integer
from sqlalchemy import Column
from core.models.baseModel import BaseModel

class Status(enum.Enum):
    open = 1
    confirm = 2
    vital_sign_complete = 3
    consultation_start = 4
    consultation_in_progress = 5
    consultation_complete = 6
    complete = 7
    cancelled = 8

class Source(enum.Enum):
    walk_in = 'walk_in'
    phone_call = 'phone_call'

class Appointment(BaseModel):
    __tablename__='appointment'

    id = Column(Integer, index=True, autoincrement=True, primary_key=True)
    patient_id = Column(Integer,ForeignKey('patient.id'))
    patient = relationship('Patient', uselist=False)
    doctor_id = Column(Integer,ForeignKey('doctor.id'))
    doctor = relationship('Doctor',uselist=False)
    appointment_time=Column(DateTime)
    status = Column(Enum(Status))
    source = Column(Enum(Source))