from uuid import UUID
from fastapi import APIRouter, Depends

from app.core.db.dependencies import get_db
from app.modules.auth.current_workspace import (
    get_current_workspace,
)
from app.modules.brand_brain.schemas import (
    BrandKnowledgeCreate,
    BrandKnowledgeUpdate
)

from app.modules.brand_brain.service import (
    create_brand_knowledge,
    get_brand_knowledge,
    update_brand_knowledge,
    delete_brand_knowledge,
)

router = APIRouter(
    prefix="/brand-brain",
    tags=["Brand Brain"]
)


@router.post("/")
async def create_brand_brain(
    payload: BrandKnowledgeCreate,
    workspace_id=Depends(get_current_workspace),
    session=Depends(get_db),
):
    knowledge_id = await create_brand_knowledge(
        session=session,
        payload=payload,
        
    )

    return {
        "knowledge_id": str(knowledge_id)
    }


@router.get("/{brand_id}")
async def get_brand_brain(
    brand_id: UUID,
    session=Depends(get_db),
    workspace_id=Depends(get_current_workspace)
):
    return await get_brand_knowledge(
        session=session,
        brand_id=brand_id,
       
    )


@router.put("/{brand_id}")
async def update_brand_brain(
    brand_id: UUID,
    payload: BrandKnowledgeUpdate,
    session=Depends(get_db),
    workspace_id=Depends(get_current_workspace)
):
    return await update_brand_knowledge(
        session=session,
        brand_id=brand_id,
        payload=payload,
        
    )


@router.delete("/{brand_id}")
async def delete_brand_brain(
    brand_id: UUID,
    session=Depends(get_db),
    workspace_id=Depends(get_current_workspace)
):
    return await delete_brand_knowledge(
        session=session,
        brand_id=brand_id,
        
    )