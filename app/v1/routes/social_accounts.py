from uuid import UUID
from fastapi import APIRouter, Depends

from app.core.db.dependencies import get_db
from app.modules.auth.current_workspace import get_current_workspace
from app.modules.social_accounts.schemas import (
    SocialAccountCreate,
    SocialAccountUpdate
)

from app.modules.social_accounts.service import (
    SocialAccountService
)

router = APIRouter(
    prefix="/social-accounts",
    tags=["Social Accounts"]
)


@router.post("/")
async def create_social_account(
    payload: SocialAccountCreate,
    workspace_id=Depends(get_current_workspace),
    session=Depends(get_db)
):
    return await SocialAccountService.create(session, workspace_id, payload)


@router.get("/{social_account_id}")
async def get_social_account(
    social_account_id: UUID,
    workspace_id=Depends(get_current_workspace),
    session=Depends(get_db)
):
    return await SocialAccountService.get(session, workspace_id, social_account_id)

@router.get("/")
async def list_social_accounts(
    workspace_id: UUID,
    session=Depends(get_db)
):
    return await SocialAccountService.list(
        session=session,
        workspace_id=workspace_id
    )

@router.put("/{social_account_id}")
async def update_social_account(
    social_account_id: UUID,
    payload: SocialAccountUpdate,
    workspace_id=Depends(get_current_workspace),
    session=Depends(get_db)
):
    return await SocialAccountService.update(
        session,
        workspace_id,
        social_account_id,
        payload
    )


@router.delete("/{social_account_id}")
async def delete_social_account(
    social_account_id: UUID,
    workspace_id=Depends(get_current_workspace),
    session=Depends(get_db)
):
    return await SocialAccountService.delete(
        session,
        workspace_id,
        social_account_id
    )