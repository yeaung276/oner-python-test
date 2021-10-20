from typing import List
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from core.models import get_db, User, Department
from core.schemas.HR.common import DepartmentSch
from api.exceptions.common import not_found_exception
from utils.auth import check_auth
from utils.db import updateItem

deptRoute = APIRouter(
    prefix='/HR',
    tags=['HR'],
)

@deptRoute.post('/department')
def addDepartment(name:str,description:str, db:Session=Depends(get_db), user:User=Depends(check_auth(['admin']))):
    new_department = Department(name=name,description=description)
    new_department.set_stamp(user)
    db.add(new_department)
    db.commit()
    db.refresh(new_department)
    return new_department

@deptRoute.put('/depatment/{id}')
def updateDepartment(id:int,new_dept:DepartmentSch, db:Session=Depends(get_db), user:User=Depends(check_auth(['admin']))):
    dept = db.query(Department).get(id)
    if dept==None:
        raise not_found_exception
    updateItem(dept,new_dept.dict(exclude_unset=True))
    dept.update_stamp(user)
    return {'message':'done'}

@deptRoute.delete('/department/{id}')
def deleteDepartment(id:int,db:Session=Depends(get_db), user:User=Depends(check_auth(['admin']))):
    dept = db.query(Department).get(id)
    if dept==None:
        raise not_found_exception
    db.delete(dept)
    return {'message':'done'}

@deptRoute.get('/department', response_model=List[DepartmentSch])
def getPositions(db:Session=Depends(get_db), user:User=Depends(check_auth(['admin']))):
    return db.query(Department).all()