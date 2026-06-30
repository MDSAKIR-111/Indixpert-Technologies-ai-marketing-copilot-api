from uuid import UUID

from fastapi import APIRouter, Depends

from app.core.db.dependencies import get_db
from app.modules.auth.current_workspace import get_current_workspace
from app.modules.dashboard.service import DashboardService

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/overview")
async def dashboard_overview(
    workspace_id=Depends(get_current_workspace),
    session=Depends(get_db)
):
    return await DashboardService.overview(
        session,
        workspace_id
    )


@router.get("/recent-activity")
async def recent_activity(
    workspace_id=Depends(get_current_workspace),
    session=Depends(get_db)
):
    return await DashboardService.recent_activity(
        session,
        workspace_id
    )