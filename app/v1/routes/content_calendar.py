from uuid import UUID
from fastapi import APIRouter, Depends

from app.core.db.dependencies import get_db
from app.modules.auth.current_workspace import get_current_workspace

from app.modules.content_calendar.schemas import (
    ContentCalendarCreate,
    ContentCalendarUpdate,
)

from app.modules.content_calendar.service import (
    ContentCalendarService,
)

router = APIRouter(
    prefix="/content-calendar",
    tags=["Content Calendar"],
)


@router.post("/")
async def create_content_calendar(
    payload: ContentCalendarCreate,
    session=Depends(get_db),
    workspace_id=Depends(get_current_workspace),
):
    return await ContentCalendarService.create(
        session=session,
        workspace_id=workspace_id,
        payload=payload,
    )


@router.get("/")
async def list_content_calendar(
    session=Depends(get_db),
    workspace_id=Depends(get_current_workspace),
):
    return await ContentCalendarService.list(
        session=session,
        workspace_id=workspace_id,
    )


@router.get("/{calendar_id}")
async def get_content_calendar(
    calendar_id: UUID,
    session=Depends(get_db),
    workspace_id=Depends(get_current_workspace),
):
    return await ContentCalendarService.get(
        session=session,
        workspace_id=workspace_id,
        calendar_id=calendar_id,
    )


@router.put("/{calendar_id}")
async def update_content_calendar(
    calendar_id: UUID,
    payload: ContentCalendarUpdate,
    session=Depends(get_db),
    workspace_id=Depends(get_current_workspace),
):
    return await ContentCalendarService.update(
        session=session,
        workspace_id=workspace_id,
        calendar_id=calendar_id,
        payload=payload,
    )


@router.delete("/{calendar_id}")
async def delete_content_calendar(
    calendar_id: UUID,
    session=Depends(get_db),
    workspace_id=Depends(get_current_workspace),
):
    return await ContentCalendarService.delete(
        session=session,
        workspace_id=workspace_id,
        calendar_id=calendar_id,
    )