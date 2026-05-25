from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

class CreateConnection(BaseModel):
    id: int
    application_id: UUID
    connector_id: int