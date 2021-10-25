from sqlalchemy.orm import Session
from app.models.baseModel import BaseModel, User

class CRUDService:
    def __init__(self,db:Session,user:User):
        self.db = db
        self.user = user

    def getAll(self,model:BaseModel):
        return self.db.query(model).all()

    def get(self,model:BaseModel,id:int):
        return self.db.query(model).get(id)

    def add(self,model:BaseModel):
        return model.add(self.user,self.db)

    def update(self,model:BaseModel,data:dict):
        return model.update(data,self.user,self.db)

    def delete(self,model:BaseModel):
        self.db.delete(model)