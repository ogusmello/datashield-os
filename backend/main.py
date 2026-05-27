from fastapi import FastAPI, APIRouter

from modules.core.database import engine
from modules.core.models import BaseModel

from modules.application.controllers import (
    connector_router,
    application_router,
    connection_router,
    application_leaf_router,
    application_leaf_review_router
)

from modules.users.controllers.user import user_router

BaseModel.metadata.create_all(bind=engine)

app = FastAPI(
    title="DataShield OS API", 
    version="0.0.1"
)

api_router = APIRouter(prefix='/api')

@api_router.get('/health')
def health_check():
    return 'API Running'

app.include_router(router=api_router, tags=["API"])

app.include_router(router=connector_router, prefix='/connector', tags=["Connectors"])
app.include_router(router=application_router, prefix='/application', tags=["Applications"])
app.include_router(router=connection_router, prefix='/connection', tags=["Connections"])
app.include_router(router=user_router, prefix='/user', tags=["Users"])
app.include_router(router=application_leaf_router, prefix='/application/leaf', tags=["Application Leaf"])
app.include_router(router=application_leaf_review_router, prefix='/application/leaf/review', tags=["Application Leaf Reviews"])