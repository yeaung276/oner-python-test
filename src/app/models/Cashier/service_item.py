import enum
from sqlalchemy import Column, String, Enum, Integer
from app.models.baseModel import BaseModel

class accounting_category(enum.Enum):
    consultation = 'Consultation'
    opd = "Opd"
    room_charges = "Room Changes"
    haemo = "Haemo"
    endo = "Endo"
    ct = "CT"
    x_ray = "X-Ray"
    ultrasound = "Ultrasound"
    ecg = "Ecg"
    pharmacy = "Pharmacy"
    lab = "Lab"

class ServiceItem(BaseModel):
    __tablename__='service_item'
    id=Column(Integer, index=True, autoincrement=True, primary_key=True)
    name=Column(String)
    service_type=Column(String)
    relation_id=Column(Integer)
    accounting_category=Column(Enum(accounting_category))
    charge=Column(Integer)