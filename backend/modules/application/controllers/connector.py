from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from modules.core.database import get_db
from modules.application.models.connector import Connector
from modules.application.schemas.connector import UpdateConnector, CreateConnector

connector_router = APIRouter()

@connector_router.get('/')
def get_all_connectors(db: Session = Depends(get_db)):
    return db.query(Connector).all()

@connector_router.get('/{id}')
def get_connector_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(Connector).filter(Connector.id == id).first()

@connector_router.post('/')
def create_connector(connector_obj: CreateConnector, db: Session = Depends(get_db)):
    connector = Connector(name=connector_obj.name)
    
    db.add(connector)
    db.commit()
    db.refresh(connector)

    return connector

@connector_router.patch('/{id}')
def update_connector_by_id(id: int, connector_obj: UpdateConnector, db: Session = Depends(get_db)):
    db_connector = db.query(Connector).filter(Connector.id == id).first()

    if(db_connector):
        db_connector.name = connector_obj.name
        db.commit()
        db.refresh(db_connector)
        return db_connector
    
    return 'Connector does not exists'

@connector_router.delete('/{id}')
def delete_connector_by_id(id: int, db: Session = Depends(get_db)):
    db_connector = db.query(Connector).filter(Connector.id == id).first()

    if(db_connector):
        db.delete(db_connector)
        db.commit()

        return 'Connector deleted'
    
    return 'Connector does not exists'