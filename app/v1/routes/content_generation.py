from uuid import UUID
from fastapi import APIRouter, Depends

from app.core.db.dependencies import get_db
from app.modules.content_generation.ai_service import (
    ContentGenerationAIService
)
from app.modules.content_generation.schemas import (
    GeneratedContentCreate,
    GenerateContentRequest,
    RegenerateContentRequest,
    GeneratedContentUpdate,
    EditContentRequest
   
)


from app.modules.content_generation.service import (
    ContentGenerationService
)



router = APIRouter(
    prefix="/generated-content",
    tags=["Generated Content"]
)





@router.get("/{content_id}")
async def get_generated_content(
    content_id: UUID,
    session=Depends(get_db)
):
    return await ContentGenerationService.get(
        session,
        content_id
    )


@router.get("/brand/{brand_id}")
async def list_generated_content(
    brand_id: UUID,
    session=Depends(get_db)
):
    return await ContentGenerationService.list(
        session,
        brand_id
    )

@router.post("/generate")
async def generate_content(
    payload: GenerateContentRequest,
    session=Depends(get_db)
):
    return await ContentGenerationAIService.generate(
        session,
        payload
    )


@router.get("/{content_id}/versions")
async def get_versions(
    content_id: UUID,
    session=Depends(get_db)
):
    return await ContentGenerationService.get_versions(
        session,
        content_id
    )

@router.post("/{content_id}/regenerate")
async def regenerate_content(
    content_id: UUID,
    payload: RegenerateContentRequest,
    session=Depends(get_db)
):
    return await ContentGenerationService.regenerate(
        session=session,
        content_id=content_id,
        prompt=payload.prompt,
    )

@router.put("/{content_id}")
async def update_generated_content(
    content_id: UUID,
    payload: GeneratedContentUpdate,
    session=Depends(get_db)
):
    return await ContentGenerationService.update(
        session,
        content_id,
        payload.generated_text
    )

@router.post("/{content_id}/edit")
async def edit_content(
    content_id: UUID,
    payload: EditContentRequest,
    session=Depends(get_db)
):
    return await ContentGenerationAIService.edit(
        session=session,
        content_id=content_id,
        instruction=payload.instruction,
    )