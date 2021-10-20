from sqlalchemy.orm.session import sessionmaker
from database import engine
from core.models.baseModel import *

# HR models
from core.models.HR.department import *
from core.models.HR.position import *
from core.models.HR.employee import * 

# emr models
from core.models.EMR.patient import *

Base.metadata.create_all(bind=engine, checkfirst=True)


