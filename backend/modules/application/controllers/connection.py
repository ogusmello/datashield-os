from uuid import uuid4, UUID
from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from modules.core.database import get_db
from modules.application.models.connection import Connection
from modules.application.models.connector import Connector
from modules.application.models.application import Application
from modules.application.schemas.connection import CreateConnection

connection_router = APIRouter()

@connection_router.get('/')
def get_all_connection(db: Session = Depends(get_db)):
    return db.query(Connection).all()

@connection_router.get('/{id}')
def get_connection_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(Connection).filter(Connection.id == id).first()

@connection_router.post('/')
def create_connection(connection_obj: CreateConnection, db: Session = Depends(get_db)):
    if not (db.query(Application).filter(Application.id == connection_obj.application_id).first()):
        return 'Application not found'
    
    if not (db.query(Connector).filter(Connector.id == connection_obj.connector_id).first()):
        return 'Connector not found'

    connection = Connection(
        application_id = connection_obj.application_id,
        connector_id = connection_obj.connector_id,
        created_at = datetime.now()
    )

    db.add(connection)
    db.commit()
    db.refresh(connection)

    return connection

@connection_router.delete('/{id}')
def delete_connection_by_id(id: int, db: Session = Depends(get_db)):
    db_connection = db.query(Connection).filter(Connection.id == id).first()

    if(db_connection):
        db.delete(db_connection)
        db.commit()

        return 'Connection deleted'
    
    return 'Connection does not exists'