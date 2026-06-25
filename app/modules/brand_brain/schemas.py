from pydantic import BaseModel


class BrandKnowledgeCreate(BaseModel):
    brand_id: str

    company_description: str
    target_audience: str
    products_services: str
    brand_voice: str
    competitors: str
    ai_instructions: str