from uuid import UUID
from fastapi import APIRouter, Depends

from app.core.db.dependencies import get_db

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
    session=Depends(get_db)
):
    return await SocialAccountService.create(session, payload)


@router.get("/{social_account_id}")
async def get_social_account(
    social_account_id: UUID,
    session=Depends(get_db)
):
    return await SocialAccountService.get(session, social_account_id)


@router.put("/{social_account_id}")
async def update_social_account(
    social_account_id: UUID,
    payload: SocialAccountUpdate,
    session=Depends(get_db)
):
    return await SocialAccountService.update(
        session,
        social_account_id,
        payload
    )


@router.delete("/{social_account_id}")
async def delete_social_account(
    social_account_id: UUID,
    session=Depends(get_db)
):
    return await SocialAccountService.delete(
        session,
        social_account_id
    )