from fastapi import FastAPI, Depends
import uvicorn

from api.controllers.auth import auth
from api.controllers.HR.position import posRoute
from api.controllers.HR.department import deptRoute
from api.controllers.HR.employee import empRoute
from sqlalchemy.orm import Session
from core.models import get_db,User,Role


import os
from utils.auth import check_auth


app = FastAPI()

app.include_router(auth)
app.include_router(posRoute)
app.include_router(deptRoute)
app.include_router(empRoute)

@app.get('/')
def index():
    return 'Welcome from Oner Hospital Management Software.'


@app.get('/role')
def getRoles(db:Session=Depends(get_db), user:User=Depends(check_auth(['test']))):
    print(user.id)
    return db.query(Role).all()
    


if __name__=='__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8080, reload=True, log_level='info')