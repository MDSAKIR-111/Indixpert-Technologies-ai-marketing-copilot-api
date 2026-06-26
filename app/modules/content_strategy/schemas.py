from pydantic import BaseModel
from uuid import UUID


class ContentStrategyCreate(BaseModel):
    brand_id: UUID
    strategy_name: str
    goal: str
    content_pillars: str
    posting_frequency: str
    platforms: str