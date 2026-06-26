from uuid import UUID
from pydantic import BaseModel


class GeneratedContentCreate(BaseModel):
    brand_id: UUID
    content_type: str
    prompt: str
    generated_text: str
    platform: str


class GenerateContentRequest(BaseModel):
    brand_id: UUID
    content_type: str
    prompt: str
    platform: str


class RegenerateContentRequest(BaseModel):
    prompt: str


class GeneratedContentUpdate(BaseModel):
    generated_text: str
    status: str


class EditContentRequest(BaseModel):
    instruction: str