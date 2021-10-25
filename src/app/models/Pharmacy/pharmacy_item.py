from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from app.models.baseModel import BaseModel

class PharmacyItem(BaseModel):
    __tablename__='pharmacy_item'

    category_id=Column(Integer,ForeignKey('pharmacy_category.id'))
    category=relationship('PharmacyCategory')
    product_code=Column(String)
    brand_name=Column(String)
    generic_name=Column(String)
    form=Column(String)
    strength=Column(String)
    packaging=Column(String)
    unit=Column(String)