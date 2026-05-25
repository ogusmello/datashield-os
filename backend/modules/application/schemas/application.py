from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

class CreateApplication(BaseModel):
    id: UUID
    name: str