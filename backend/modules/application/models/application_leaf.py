from uuid import UUID as uuid
from datetime import datetime

from modules.core.models import BaseModel

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import UUID, String, Integer, ForeignKey, Boolean, DateTime

class ApplicationLeaf(BaseModel):
    __tablename__ = 'application_leafs'

    id: Mapped[uuid] = mapped_column(primary_key=True, index=True, unique=True)
    connection_id: Mapped[int] = mapped_column(ForeignKey('connections.id'), index=True)
    database: Mapped[str] = mapped_column(String)
    table: Mapped[str] = mapped_column(String)
    column: Mapped[str] = mapped_column(String)
    initial_confidence: Mapped[str] = mapped_column(String)
    initial_attribute: Mapped[str] = mapped_column(String)
    initial_pi: Mapped[int] = mapped_column(Integer)
    initial_security: Mapped[str] = mapped_column(String)
    review_status: Mapped[str] = mapped_column(String)
    last_review_id: Mapped[UUID] = mapped_column(ForeignKey('application_leaf_reviews.id'), index=True)
    new_confidence_flag: Mapped[bool] = mapped_column(Boolean)
    new_attribute_flag: Mapped[bool] = mapped_column(Boolean)
    new_pi_flag: Mapped[bool] = mapped_column(Boolean)
    new_security_flag: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)