from pydantic import BaseModel
from utils.hash import hash

class UserRegister(BaseModel):
    username: str
    fullname: str
    password: str
    role_id: int

    def get_hashed(self):
        return {
            'username': self.username,
            'fullname': self.fullname,
            'role_id': self.role_id,
            'password_hash': hash(self.password)
        }

class Login(BaseModel):
    username: str
    password: str

class CredentialReturn(BaseModel):
    username: str
    role: str
    token: str

class ChangePassword(BaseModel):
    old_password: str
    new_password: str
