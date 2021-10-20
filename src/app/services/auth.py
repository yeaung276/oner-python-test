    from sqlalchemy.orm.session import Session


def verify(self,password):
        return verify(password, self.password_hash)

def change_password(self,new_password:str,db:Session):
    self.password_hash = hash(new_password)
    db.commit()