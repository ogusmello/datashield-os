from uuid import UUID, uuid4
from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from modules.core.database import get_db
from modules.application.models.application_leaf import ApplicationLeaf
from modules.application.models.connection import Connection
from modules.application.schemas.application_leaf import CreateApplicationLeaf, UpdateApplicationLeaf

application_leaf_router = APIRouter()

@application_leaf_router.get('/{connection_id}')
def get_all_leafs_from_connection(connection_id: UUID, db: Session = Depends(get_db)):
    db_connection = db.query(Connection).filter(Connection.id == connection_id).first()

    if(db_connection):
        return db.query(ApplicationLeaf).filter(ApplicationLeaf.connection_id == connection_id).all()

    return 'Connection not found'

@application_leaf_router.get('/{id}')
def get_leaf_by_id(id: UUID, db: Session = Depends(get_db)):
    db_leaf = db.query(ApplicationLeaf).filter(ApplicationLeaf.id == id).first()

    if(db_leaf):
        return db.query(ApplicationLeaf).filter(ApplicationLeaf.id == id).first()

    return "Leaf not found"

@application_leaf_router.post('/')
def create_application_leaf(leaf_obj: CreateApplicationLeaf, db: Session = Depends(get_db)):
    leaf = ApplicationLeaf(
        id = uuid4(),
        connection_id = leaf_obj.connection_id,
        database = leaf_obj.database,
        table = leaf_obj.table,
        column = leaf_obj.column,
        initial_confidence = leaf_obj.initial_confidence,
        initial_attribute = leaf_obj.initial_attribute,
        initial_pi = leaf_obj.initial_pi,
        initial_security = leaf_obj.initial_security,
        review_status = leaf_obj.review_status,
        last_review_id = leaf_obj.last_review_id,
        new_confidence_flag = leaf_obj.new_confidence_flag,
        new_attribute_flag = leaf_obj.new_attribute_flag,
        new_pi_flag = leaf_obj.new_pi_flag,
        new_security_flag = leaf_obj.new_security_flag,
        created_at = datetime.now(),
    )

    db.add(leaf)
    db.commit()
    db.refresh(leaf)

    return leaf

@application_leaf_router.patch('/{id}')
def patch_leaf_by_id(id: UUID, leaf_obj: UpdateApplicationLeaf, db: Session = Depends(get_db)):
    db_leaf = db.query(ApplicationLeaf).filter(ApplicationLeaf.id == id).first()

    if(db_leaf):
        if(leaf_obj.review_status):
            db_leaf.review_status = leaf_obj.review_status

        if(leaf_obj.last_review_id):
            db_leaf.last_review_id = leaf_obj.last_review_id

        if(leaf_obj.new_confidence_flag):
            db_leaf.new_confidence_flag = True

        if(leaf_obj.new_attribute_flag):
            db_leaf.new_attribute_flag = True

        if(leaf_obj.new_pi_flag):
            db_leaf.new_pi_flag = leaf_obj.new_pi_flag

        if(leaf_obj.new_security_flag):
            db_leaf.new_security_flag = True

        db_leaf.updated_at = datetime.now()

        db.commit()
        db.refresh(db_leaf)

        return db_leaf
    
    return 'Leaf not found'