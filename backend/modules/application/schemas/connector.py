from pydantic import BaseModel

class ConnectorResponse(BaseModel):
    id: int
    name: str

class CreateConnector(BaseModel):
    name: str

class UpdateConnector(BaseModel):
    name: str
