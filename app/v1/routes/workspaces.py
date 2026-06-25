from fastapi import APIRouter, Depends

from app.modules.workspaces.schemas import WorkspaceCreate
from app.modules.workspaces.service import create_workspace
from app.modules.auth.dependencies import get_current_user
from app.core.db.dependencies import get_db

router = APIRouter()
router = APIRouter(
    prefix="/workspace",
    tags=["Workspace"]
)


@router.post("/")
async def create_workspace_route(
    payload: WorkspaceCreate,
    session=Depends(get_db),
):
    result = await create_workspace(
        session=session,
        workspace_name=payload.workspace_name,
        email=payload.email,
        full_name=payload.full_name,
    )

    return {
        "success": True,
        "data": result,
    }


@router.get("/me")
async def me(
    current_user=Depends(get_current_user)
):
    return current_user