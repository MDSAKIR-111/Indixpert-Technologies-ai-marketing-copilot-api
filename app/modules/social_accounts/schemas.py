from uuid import UUID
from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class SocialAccountCreate(BaseModel):
    brand_id: UUID
    platform: str
    access_token: str
    refresh_token: Optional[str] = None
    account_id: Optional[str] = None
    page_id: Optional[str] = None
    expires_at: Optional[datetime] = None


class SocialAccountUpdate(BaseModel):
    platform: str
    access_token: str
    refresh_token: Optional[str] = None
    account_id: Optional[str] = None
    page_id: Optional[str] = None
    expires_at: Optional[datetime] = None


class SocialAccountResponse(BaseModel):
    id: UUID
    brand_id: UUID
    platform: str
    account_id: Optional[str]
    page_id: Optional[str]
    expires_at: Optional[datetime]