from uuid import uuid4, UUID
from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from modules.core.database import get_db
from modules.application.models.application import Application
from modules.application.schemas.application import CreateApplication

application_router = APIRouter()

@application_router.get('/')
def get_all_application(db: Session = Depends(get_db)):
    return db.query(Application).all()

@application_router.get('/{id}')
def get_application_by_id(id: UUID, db: Session = Depends(get_db)):
    return db.query(Application).filter(Application.id == id).first()

@application_router.post('/')
def create_application(application_obj: CreateApplication, db: Session = Depends(get_db)):
    application = Application(
        id = uuid4(),
        name = application_obj.name,
        scanned_at = datetime.now()
    )

    db.add(application)
    db.commit()
    db.refresh(application)

    return application

@application_router.delete('/{id}')
def delete_application_by_id(id: UUID, db: Session = Depends(get_db)):
    db_application = db.query(Application).filter(Application.id == id).first()

    if(db_application):
        db.delete(db_application)
        db.commit()

        return 'Application deleted'
    
    return 'Application does not exists'