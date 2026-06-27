from fastapi import APIRouter, Depends
from uuid import UUID
from app.core.db.dependencies import get_db

from app.modules.content_strategy.schemas import (
    ContentStrategyCreate,
    GenerateStrategyRequest
)

from app.modules.content_strategy.service import (
    create_content_strategy,
    get_strategy,
)

from app.modules.content_strategy.ai_service import (
    ContentStrategyAIService,
)

router = APIRouter(
    prefix="/content-strategy",
    tags=["Content Strategy"]
)


@router.post("/")
async def create_strategy(
    payload: ContentStrategyCreate,
    session=Depends(get_db),
):
    strategy_id = await create_content_strategy(
        session=session,
        payload=payload
    )

    return {
        "strategy_id": str(strategy_id)
    }

@router.post("/generate")
async def generate_strategy(
    payload: GenerateStrategyRequest,
    session=Depends(get_db),
):
    return await ContentStrategyAIService.generate(
        session=session,
        payload=payload,
    )

@router.get("/{brand_id}")
async def get_content_strategy(
    brand_id: UUID,
    session=Depends(get_db),
):
    return await get_strategy(
        session=session,
        brand_id=brand_id,
    )