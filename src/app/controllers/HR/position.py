from typing import List
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from core.models import get_db, User, Position
from core.schemas.HR.common import PositionSch
from api.exceptions.common import not_found_exception
from utils.auth import check_auth
from utils.db import updateItem

posRoute = APIRouter(
    prefix='/HR',
    tags=['HR'],
)

@posRoute.post('/position')
def addPosition(name:str,description:str, db:Session=Depends(get_db), user:User=Depends(check_auth(['admin']))):
    new_position = Position(name=name,description=description)
    new_position.set_stamp(user)
    db.add(new_position)
    db.commit()
    db.refresh(new_position)
    return new_position

@posRoute.put('/position/{id}')
def updatePosition(id:int,new_pos:PositionSch, db:Session=Depends(get_db), user:User=Depends(check_auth(['admin']))):
    pos = db.query(Position).get(id)
    if pos==None:
        raise not_found_exception
    updateItem(pos, new_pos.dict(exclude_unset=True))
    pos.update_stamp(user)
    db.commit()
    return {'message':'done'}

@posRoute.delete('/position/{id}')
def deletePosition(id:int, db:Session=Depends(get_db), user:User=Depends(check_auth(['admin']))):
    pos = db.query(Position).get(id)
    if pos==None:
        raise not_found_exception
    db.delete(pos)
    return {'message': 'done'}


@posRoute.get('/position', response_model=List[PositionSch])
def getPositions(db:Session=Depends(get_db), user:User=Depends(check_auth(['admin']))):
    return db.query(Position).all()