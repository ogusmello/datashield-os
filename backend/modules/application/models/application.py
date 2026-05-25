from uuid import UUID
from datetime import datetime

from modules.core.models import BaseModel

from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

class Application(BaseModel):
    __tablename__ = 'applications'

    id: Mapped[UUID] = mapped_column(primary_key=True, unique=True, index=True)
    name: Mapped[str] = mapped_column(String)
    scanned_at: Mapped[datetime] = mapped_column(DateTime)