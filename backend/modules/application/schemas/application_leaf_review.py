from uuid import UUID
from datetime import datetime

from pydantic import BaseModel

class CreateApplicationLeafReview(BaseModel):
    id: UUID
    application_id: UUID
    reviewer_id: UUID
    reviewed_at: datetime
    prev_revision_id: UUID
    reviewed_column: str
    proposed_attribute: str
    proposed_pi: int
    proposed_confidence: str
    proposed_security: str
    review_judgment: str
    review_comment: str