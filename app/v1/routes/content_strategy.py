from fastapi import APIRouter, Depends

from app.core.db.dependencies import get_db

from app.modules.content_strategy.schemas import (
    ContentStrategyCreate
)

from app.modules.content_strategy.service import (
    create_content_strategy
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