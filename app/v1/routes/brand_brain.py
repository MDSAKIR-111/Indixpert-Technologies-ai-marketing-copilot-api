from fastapi import APIRouter, Depends

from app.core.db.dependencies import get_db

from app.modules.brand_brain.schemas import (
    BrandKnowledgeCreate
)

from app.modules.brand_brain.service import (
    create_brand_knowledge
)

router = APIRouter(
    prefix="/brand-brain",
    tags=["Brand Brain"]
)


@router.post("/")
async def create_brand_brain(
    payload: BrandKnowledgeCreate,
    session=Depends(get_db),
):
    knowledge_id = await create_brand_knowledge(
        session=session,
        payload=payload
    )

    return {
        "knowledge_id": str(knowledge_id)
    }