from uuid import UUID
from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class CreateUser(BaseModel):
    email: str
    password_hash: str
    name: str
    role: str

class UpdateUser(BaseModel):
    email: Optional[str]
    password_hash: Optional[str]
    name: Optional[str]
    role: Optional[str]
    
class LoginUser(BaseModel):
    email: str
    password: str