from modules.core.models import BaseModel

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

class Connector(BaseModel):
    __tablename__ = 'connectors'

    id: Mapped[int] = mapped_column(primary_key=True, unique=True, index=True)
    name: Mapped[str] = mapped_column(String(64), index=True)

    def __repr__(self) -> str:
        return f"Connector - {self.name}"