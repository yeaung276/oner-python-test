from fastapi import FastAPI
import uvicorn

from app.controllers.auth import auth
# from app.controllers.HR.position import posRoute
# from app.controllers.HR.department import deptRoute
# from app.controllers.HR.employee import empRoute


app = FastAPI()

app.include_router(auth)
# app.include_router(posRoute)
# app.include_router(deptRoute)
# app.include_router(empRoute)

@app.get('/')
def index():
    return 'Welcome from Oner Hospital Management Software.' 


if __name__=='__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8080, reload=True, log_level='debug')