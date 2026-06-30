"""
app/modules/social_accounts/linkedin_oauth/service.py
"""

import secrets

from fastapi import HTTPException

from app.modules.social_accounts.linkedin_oauth.client import LinkedInOAuthClient
from app.modules.social_accounts.service import SocialAccountService
from app.modules.social_accounts.schemas import SocialAccountCreate

# NOTE: Production mein Redis use karna (settings.redis_url already hai),
# abhi in-memory dict use kar rahe hain testing ke liye.
_state_store: dict[str, dict] = {}


class LinkedInOAuthService:

    @staticmethod
    def generate_connect_url(workspace_id: str, brand_id: str) -> str:
        state = secrets.token_urlsafe(24)

        _state_store[state] = {
            "workspace_id": workspace_id,
            "brand_id": brand_id,
        }

        return LinkedInOAuthClient.get_authorization_url(state=state)

    @staticmethod
    def _consume_state(state: str) -> dict:
        data = _state_store.pop(state, None)

        if not data:
            raise HTTPException(
                status_code=400,
                detail="Invalid or expired state. Dobara LinkedIn connect karo.",
            )

        return data

    @staticmethod
    async def handle_callback(session, code: str, state: str):
        state_data = LinkedInOAuthService._consume_state(state)
        workspace_id = state_data["workspace_id"]
        brand_id = state_data["brand_id"]

        token_data = await LinkedInOAuthClient.exchange_code_for_token(code)

        access_token = token_data["access_token"]
        refresh_token = token_data.get("refresh_token")
        expires_in = token_data.get("expires_in")

        expires_at = None
        if expires_in:
            from datetime import datetime, timedelta, timezone
            expires_at = datetime.now(timezone.utc) + timedelta(seconds=expires_in)

        profile = await LinkedInOAuthClient.get_user_profile(access_token)
        linkedin_user_id = profile["sub"]

        account_id = f"person:{linkedin_user_id}"

        payload = SocialAccountCreate(
            brand_id=brand_id,
            platform="linkedin",
            access_token=access_token,
            refresh_token=refresh_token,
            account_id=account_id,
            page_id=None,
            expires_at=expires_at,
        )

        result = await SocialAccountService.create(session, workspace_id, payload)

        return result