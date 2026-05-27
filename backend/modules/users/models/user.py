from datetime import datetime

from modules.core.models import BaseModel

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import UUID, String, DateTime

class User(BaseModel):
    __tablename__ = 'users'
    
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, index=True, unique=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String)
    role: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)