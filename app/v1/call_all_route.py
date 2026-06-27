from fastapi import APIRouter


from app.v1.routes.workspaces import router as workspaces_router
from app.v1.routes.auth import router as auth_router
from app.v1.routes.brands import router as brands_router
from app.v1.routes.brand_brain import (
    router as brand_brain_router
)
from app.v1.routes.content_strategy import (
    router as content_strategy_router
)
from app.v1.routes.content_calendar import (
    router as content_calendar_router
)
from app.v1.routes.content_generation import (
    router as content_generation_router
)
from app.v1.routes.social_accounts import (
    router as social_accounts_router
)
from app.v1.routes.publisher import (
    router as social_publish_router
)



api_router = APIRouter()


api_router.include_router(workspaces_router)
api_router.include_router(auth_router)
api_router.include_router(brands_router)
api_router.include_router(brand_brain_router)
api_router.include_router(
    content_strategy_router
)
api_router.include_router(
    content_calendar_router
)
api_router.include_router(
    content_generation_router
)
api_router.include_router(social_accounts_router)
api_router.include_router(social_publish_router)