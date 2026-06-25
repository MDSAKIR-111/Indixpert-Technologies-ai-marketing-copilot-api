from fastapi import APIRouter


from app.v1.routes.workspaces import router as workspaces_router
from app.v1.routes.auth import router as auth_router
from app.v1.routes.brands import router as brands_router
from app.v1.routes.brand_brain import (
    router as brand_brain_router
)

api_router = APIRouter()


api_router.include_router(workspaces_router)
api_router.include_router(auth_router)
api_router.include_router(brands_router)
api_router.include_router(brand_brain_router)