from pydantic import BaseModel
from uuid import UUID


class BrandKnowledgeCreate(BaseModel):
    brand_id: UUID
    company_description: str
    target_audience: str
    products_services: str
    brand_voice: str
    competitors: str
    ai_instructions: str


class BrandKnowledgeUpdate(BaseModel):
    company_description: str
    target_audience: str
    products_services: str
    brand_voice: str
    competitors: str
    ai_instructions: str