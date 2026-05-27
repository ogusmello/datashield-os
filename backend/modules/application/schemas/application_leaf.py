from uuid import UUID
from typing import Optional
from datetime import datetime

from pydantic import BaseModel

class CreateApplicationLeaf(BaseModel):
    id: UUID
    connection_id: int
    database: int
    table: int
    column: str
    initial_confidence: str
    initial_attribute: str
    initial_pi: int
    initial_security: str
    review_status: str
    last_review_id: UUID
    new_confidence_flag: bool
    new_attribute_flag: bool
    new_pi_flag: bool
    new_security_flag: bool
    created_at: datetime

class UpdateApplicationLeaf(BaseModel):
    review_status: Optional[str]
    last_review_id: Optional[UUID]
    new_confidence_flag: Optional[bool]
    new_attribute_flag: Optional[bool]
    new_pi_flag: Optional[bool]
    new_security_flag: Optional[bool]
    updated_at: datetime
