from uuid import UUID

from fastapi import APIRouter, Depends
from app.modules.auth.current_workspace import get_current_workspace
from app.core.db.dependencies import get_db

from app.modules.publisher.service import PublisherService

router = APIRouter(
    prefix="/publisher",
    tags=["Publisher"]
)


@router.post("/publish/{calendar_id}")
async def publish(
    calendar_id: UUID,
    session=Depends(get_db),
    workspace_id=Depends(get_current_workspace)
):
    return await PublisherService.publish(
        session=session,
        workspace_id=workspace_id,
        calendar_id=calendar_id,
    )

@router.get("/logs")
async def get_logs(
    session=Depends(get_db),
    workspace_id=Depends(get_current_workspace)
):
    return await PublisherService.get_logs(
        session=session,
        workspace_id=workspace_id,
    )