from uuid import UUID
from datetime import date
from pydantic import BaseModel


class ContentCalendarCreate(BaseModel):
    brand_id: UUID
    title: str
    content_type: str
    platform: str
    scheduled_date: date


from datetime import date
from typing import Optional
from pydantic import BaseModel


class ContentCalendarUpdate(BaseModel):
    title: str
    content_type: str
    platform: str
    scheduled_date: date
    status: Optional[str] = "draft"


class ContentCalendarResponse(BaseModel):
    id: UUID
    brand_id: UUID
    title: str
    content_type: str
    platform: str
    scheduled_date: date
    status: str