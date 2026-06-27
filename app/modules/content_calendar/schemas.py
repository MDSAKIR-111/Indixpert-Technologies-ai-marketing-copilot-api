from uuid import UUID
from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ContentCalendarCreate(BaseModel):
    generated_content_id: UUID
    scheduled_datetime: datetime


class ContentCalendarUpdate(BaseModel):
    scheduled_datetime: datetime
    status: Optional[str] = "scheduled"


class ContentCalendarResponse(BaseModel):
    id: UUID
    generated_content_id: UUID
    brand_id: UUID
    title: str
    content_type: str
    platform: str
    scheduled_datetime: datetime
    status: str