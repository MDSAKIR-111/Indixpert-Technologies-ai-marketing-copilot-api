from uuid import UUID

from fastapi import APIRouter, Depends

from app.core.db.dependencies import get_db
from app.modules.publisher.service import PublisherService

router = APIRouter(
    prefix="/publisher",
    tags=["Publisher"]
)


@router.post("/publish/{calendar_id}")
async def publish(
    calendar_id: UUID,
    session=Depends(get_db)
):
    return await PublisherService.publish(
        session=session,
        calendar_id=calendar_id
    )