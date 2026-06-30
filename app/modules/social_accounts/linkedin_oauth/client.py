"""
app/modules/social_accounts/linkedin_oauth/client.py

Yeh file LinkedIn ke saath "login/permission" ki baat karti hai.
Do kaam karti hai:
  1. Authorization URL banana (jahan user ko bhejna hai)
  2. Code ko access_token mein convert karna (LinkedIn se token maangna)
"""

import httpx
from urllib.parse import urlencode
from fastapi import HTTPException

from app.core.config.settings import settings

LINKEDIN_AUTH_BASE = "https://www.linkedin.com/oauth/v2"
LINKEDIN_API_BASE = "https://api.linkedin.com/v2"

# Scopes: w_member_social = personal profile pe post karne ki permission
#         openid, profile = user ki basic identity (id, name) lene ke liye
LINKEDIN_SCOPES = "openid profile w_member_social"


class LinkedInOAuthClient:

    @staticmethod
    def get_authorization_url(state: str) -> str:
        """
        Yeh URL banata hai jahan user ko redirect karna hai.
        'state' ek random string hai jo security ke liye hai (CSRF protection).
        """
        params = {
            "response_type": "code",
            "client_id": settings.LINKEDIN_CLIENT_ID,
            "redirect_uri": settings.LINKEDIN_REDIRECT_URI,
            "state": state,
            "scope": LINKEDIN_SCOPES,
        }
        return f"{LINKEDIN_AUTH_BASE}/authorization?{urlencode(params)}"

    @staticmethod
    async def exchange_code_for_token(code: str) -> dict:
        """
        LinkedIn se mila hua temporary 'code' ko asli access_token mein
        convert karta hai.
        """
        url = f"{LINKEDIN_AUTH_BASE}/accessToken"

        data = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": settings.LINKEDIN_REDIRECT_URI,
            "client_id": settings.LINKEDIN_CLIENT_ID,
            "client_secret": settings.LINKEDIN_CLIENT_SECRET,
        }

        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(url, data=data, headers=headers)

        if response.status_code != 200:
            raise HTTPException(
                status_code=400,
                detail=f"LinkedIn token exchange failed: {response.text}",
            )

        return response.json()

    @staticmethod
    async def refresh_access_token(refresh_token: str) -> dict:
        """
        Purana token expire ho jaye toh naya lene ke liye.
        """
        url = f"{LINKEDIN_AUTH_BASE}/accessToken"

        data = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "client_id": settings.LINKEDIN_CLIENT_ID,
            "client_secret": settings.LINKEDIN_CLIENT_SECRET,
        }

        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(url, data=data, headers=headers)

        if response.status_code != 200:
            raise HTTPException(
                status_code=400,
                detail=f"LinkedIn token refresh failed: {response.text}",
            )

        return response.json()

    @staticmethod
    async def get_user_profile(access_token: str) -> dict:
        """
        Token use karke LinkedIn se user ki identity (id, name) leta hai.
        """
        url = f"{LINKEDIN_API_BASE}/userinfo"
        headers = {"Authorization": f"Bearer {access_token}"}

        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.get(url, headers=headers)

        if response.status_code != 200:
            raise HTTPException(
                status_code=400,
                detail=f"LinkedIn profile fetch failed: {response.text}",
            )

        return response.json()