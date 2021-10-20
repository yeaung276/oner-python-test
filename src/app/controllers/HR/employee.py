from typing import List
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from core.models import get_db, User
from core.models.HR.employee import Employee
from core.schemas.HR.common import EmployeeCommonSch, EmployeeDetailSch, EmployeeInputSch
from api.exceptions.common import not_found_exception
from utils.auth import check_auth
from utils.db import updateItem

empRoute = APIRouter(
    prefix='/HR',
    tags=['HR'],
)

@empRoute.post('/employee')
def adEmployee(emp:EmployeeInputSch, db:Session=Depends(get_db), user:User=Depends(check_auth(['admin']))):
    new_employee = Employee(**emp.dict())
    new_employee.set_stamp(user)
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

@empRoute.put('/employee/{id}')
def updatEmployee(id:int,new_emp:EmployeeInputSch, db:Session=Depends(get_db), user:User=Depends(check_auth(['admin']))):
    emp = db.query(Employee).get(id)
    if emp==None:
        raise not_found_exception
    updateItem(emp, new_emp.dict(exclude_unset=True))
    emp.update_stamp(user)
    return {'message':'done'}

@empRoute.delete('/employee/{id}')
def deletEmployee(id:int, db:Session=Depends(get_db), user:User=Depends(check_auth(['admin']))):
    emp = db.query(Employee).get(id)
    if emp==None:
        raise not_found_exception
    db.delete(emp)
    return {'message': 'done'}


@empRoute.get('/employee', response_model=List[EmployeeCommonSch])
def getEmployee(db:Session=Depends(get_db), user:User=Depends(check_auth(['admin']))):
    return db.query(Employee).all()

@empRoute.get('/employee/{id}', response_model=EmployeeDetailSch)
def getEmployeeById(id:int, db:Session=Depends(get_db), user:User=Depends(check_auth(['admin']))):
    emp = db.query(Employee).get(id)
    if emp==None:
        raise not_found_exception
    return emp