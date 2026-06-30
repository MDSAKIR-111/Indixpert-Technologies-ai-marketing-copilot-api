from fastapi import APIRouter, Depends

from app.modules.workspaces.schemas import WorkspaceCreate
from app.modules.workspaces.service import create_workspace
from app.modules.auth.dependencies import get_current_user
from app.core.db.dependencies import get_db


router = APIRouter(
    prefix="/workspace",
    tags=["Workspace"]
)


@router.post("/")
async def create_workspace_route(
    payload: WorkspaceCreate,
    current_user=Depends(get_current_user),
    session=Depends(get_db),
):

    result = await create_workspace(
        session=session,
        user_id=current_user["user_id"],
        workspace_name=payload.workspace_name,
    )

    return {
        "success": True,
        "current_user": current_user,
        "data": result,
    }


@router.get("/me")
async def me(
    current_user=Depends(get_current_user)
):
    return current_user

