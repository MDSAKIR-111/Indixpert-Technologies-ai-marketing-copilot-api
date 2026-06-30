"""
app/v1/routes/linkedin_oauth.py
"""

from uuid import UUID

from fastapi import APIRouter, Depends, Query
from fastapi.responses import RedirectResponse

from app.core.db.dependencies import get_db
from app.modules.auth.current_workspace import get_current_workspace
from app.modules.social_accounts.linkedin_oauth.service import LinkedInOAuthService

router = APIRouter(
    prefix="/linkedin-oauth",
    tags=["LinkedIn OAuth"]
)


@router.get("/connect")
async def connect_linkedin(
    brand_id: UUID,
    workspace_id=Depends(get_current_workspace)
):
    auth_url = LinkedInOAuthService.generate_connect_url(
        workspace_id=str(workspace_id),
        brand_id=str(brand_id),
    )
    return RedirectResponse(url=auth_url)


@router.get("/callback")
async def linkedin_callback(
    code: str = Query(...),
    state: str = Query(...),
    session=Depends(get_db)
):
    result = await LinkedInOAuthService.handle_callback(session, code, state)

    return {
        "message": "LinkedIn account connected successfully",
        "social_account": result,
    }