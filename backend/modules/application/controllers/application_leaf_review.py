from uuid import UUID, uuid4
from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from modules.core.database import get_db
from modules.application.models.application_leaf_review import ApplicationLeafReview
from modules.application.models.application import Application
from modules.application.schemas.application_leaf_review import CreateApplicationLeafReview

application_leaf_review_router = APIRouter()

@application_leaf_review_router.get('/{application_id}')
def get_all_leaf_reviews(application_id: UUID, db: Session = Depends(get_db)):
    db_application = db.query(Application).filter(Application.id == application_id).first()

    if(db_application):
        return db.query(ApplicationLeafReview).filter(ApplicationLeafReview.application_id == application_id).all()
    
    return 'Application not found'

@application_leaf_review_router.get('/{id}')
def get_leaf_review_by_id(id: UUID, db: Session = Depends(get_db)):
    return db.query(ApplicationLeafReview).filter(ApplicationLeafReview.id == id).first()

@application_leaf_review_router.post('/')
def create_leaf_review(review_obj: CreateApplicationLeafReview, db: Session = Depends(get_db)):
    review = ApplicationLeafReview(
        id = uuid4(),
        application_id = review_obj.application_id,
        reviewer_id = review_obj.reviewer_id,
        reviewed_at = datetime.now(),
        prev_revision_id = review_obj.prev_revision_id,
        reviewed_column = review_obj.reviewed_column,
        proposed_attribute = review_obj.proposed_attribute,
        proposed_pi = review_obj.proposed_pi,
        proposed_confidence = review_obj.proposed_confidence,
        proposed_security = review_obj.proposed_confidence,
        review_judgment = review_obj.review_judgment,
        review_comment = review_obj.review_comment,
    )

    db.add(review)
    db.commit()
    db.refresh(review)

    return review