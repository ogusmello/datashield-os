from uuid import UUID as uuid
from datetime import datetime

from modules.core.models import BaseModel

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import UUID, String, Integer, ForeignKey, Boolean, DateTime

class ApplicationLeafReview(BaseModel):
    __tablename__ = 'application_leaf_reviews'

    id: Mapped[uuid] = mapped_column(UUID(as_uuid=True), primary_key=True, index=True, unique=True)
    application_id: Mapped[uuid] = mapped_column(ForeignKey('applications.id'), index=True)
    reviewer_id: Mapped[uuid] = mapped_column(ForeignKey('users.id'), index=True)
    reviewed_at: Mapped[datetime] = mapped_column(DateTime)
    prev_revision_id: Mapped[uuid] = mapped_column(ForeignKey('application_leaf_reviews.id'), index=True)
    reviewed_column: Mapped[str] = mapped_column(String)
    proposed_attribute: Mapped[str] = mapped_column(String)
    proposed_pi: Mapped[int] = mapped_column(Integer)
    proposed_confidence: Mapped[str] = mapped_column(String)
    proposed_security: Mapped[str] = mapped_column(String)
    review_judgment: Mapped[str] = mapped_column(String)
    review_comment: Mapped[str] = mapped_column(String)