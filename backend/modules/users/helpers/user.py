from uuid import UUID

from pwdlib import PasswordHash
from sqlalchemy.orm import Session
from fastapi import Depends

from modules.users.models.user import User
from modules.core.database import get_db

class PasswordManager():
    def __init__(self):
        self.password_hash = PasswordHash.recommended()
        
    def get_password_hash(self, password: str) -> str:
        return self.password_hash.hash(password)
    
    def verify_password(self, plain_pwd: str, hashed_pwd: str) -> bool:
        return self.password_hash.verify(plain_pwd, hashed_pwd)
    
class UserControllerHelpers():
    def __init__(self):
        self.password_manager = PasswordManager()
        
    def verify_email(self, id, email, db: Session):
        email = db.query(User).filter(User.id == id).filter(User.email == email).first()
        
        if not email:
            return False
        
        return True
        
    def verify_password(self, id, plain_pwd: str, db: Session):
        db_user = db.query(User).filter(User.id == id).first()
        if not db_user:
            return 'User not found'
        
        pwd_hash = db_user.password_hash
        verified_pwd = self.password_manager.verify_password(plain_pwd, pwd_hash)
        
        if not verified_pwd:
            return False
        
        return True