from uuid import UUID, uuid4
from datetime import datetime

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from modules.users.models.user import User
from modules.users.schemas.user import CreateUser, UpdateUser
from modules.core.database import get_db

user_router = APIRouter()

@user_router.get('/')
def get_all_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@user_router.get('/{id}')
def get_user_by_id(id: UUID, db: Session = Depends(get_db)):
    return db.query(User).filter(User.id == id).first()

@user_router.post('/')
def create_user(user_obj: CreateUser, db: Session = Depends(get_db)):
    user = User(
        id = uuid4(),
        email = user_obj.email,
        password_hash = user_obj.password_hash,
        name = user_obj.name,
        role = user_obj.role,
        created_at = datetime.now(),
    )

    db.add(user)
    db.commit()
    db.refresh()

    return {"message": "User created", "data": user}

@user_router.patch('/{id}')
def patch_user_by_id(id: UUID, user_obj: UpdateUser, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == id).first()

    if(db_user):
        if(user_obj.name):
            db_user.name = user_obj.name

        if(user_obj.email):
            db_user.email = user_obj.email

        if(user_obj.email):
            db_user.email = user_obj.email

        if(user_obj.password_hash):
            db_user.password_hash = user_obj.password_hash

        if(user_obj.role):
            db_user.role = user_obj.role

        db.updated_at = datetime.now()

        db.commit()
        db.refresh(db_user)

        return db_user

    return 'User not found'
    


@user_router.delete('/{id}')
def delete_user_by_id(id: UUID, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == id).first()

    if(db_user):
        db.delete(db_user)
        db.commit()
        db.refresh()
        return 'User Deleted'
    
    return 'User not found.'