from datetime import datetime
from uuid import UUID

from modules.core.models import BaseModel

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, DateTime, UUID, ForeignKey

class Connection(BaseModel):
    __tablename__ = 'connections'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, unique=True)
    application_id: Mapped[UUID]  = mapped_column(ForeignKey('applications.id'), index=True)
    connector_id: Mapped[int]  = mapped_column(ForeignKey('connectors.id'), index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime)