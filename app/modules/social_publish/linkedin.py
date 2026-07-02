"""
app/modules/social_publish/linkedin.py

LinkedIn par text post publish karne ka logic.
"""

import httpx
from fastapi import HTTPException

LINKEDIN_API_BASE = "https://api.linkedin.com/v2"


class LinkedInPublisher:

    @staticmethod
    async def publish_text(account_id: str, access_token: str, message: str) -> dict:
        """
        account_id format: "person:V_vkGdpv-Y"  ->  author urn: "urn:li:person:V_vkGdpv-Y"
        """
        if not account_id or ":" not in account_id:
            raise Exception("Invalid LinkedIn account_id, cannot build author URN.")

        person_id = account_id.split(":", 1)[1]
        author_urn = f"urn:li:person:{person_id}"

        url = f"{LINKEDIN_API_BASE}/ugcPosts"

        payload = {
            "author": author_urn,
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {
                        "text": message
                    },
                    "shareMediaCategory": "NONE"
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
            }
        }

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "X-Restli-Protocol-Version": "2.0.0",
        }

        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(url, json=payload, headers=headers)

        if response.status_code not in (200, 201):
            raise HTTPException(
                status_code=400,
                detail=f"LinkedIn publish failed: {response.text}",
            )

        post_id = response.headers.get("x-restli-id")

        return {"post_id": post_id}