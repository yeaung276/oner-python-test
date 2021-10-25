from database import engine
from app.models.baseModel import *

# HR models
from app.models.HR.department import *
from app.models.HR.position import *
from app.models.HR.employee import * 

# EMR models
from app.models.EMR.patient import *
from app.models.EMR.prescription import *
from app.models.EMR.medical_record import *
from app.models.EMR.investigation_results import *

# cashier models
from app.models.Cashier.bill import *
from app.models.Cashier.deposit import *
from app.models.Cashier.payment import *
from app.models.Cashier.service_item import *
from app.models.Cashier.service_used_record import *

# OPD models
from app.models.OPD.appointment import *
from app.models.OPD.doctor import *

# Orders models
from app.models.Orders.investigation_category import *
from app.models.Orders.investigation_item import *
from app.models.Orders.investigation_order import *
from app.models.Orders.investigation_type import *

# Pharmacy models
from app.models.Pharmacy.pharmacy_category import *
from app.models.Pharmacy.pharmacy_item import *

Base.metadata.create_all(bind=engine, checkfirst=True)


