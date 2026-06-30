from fastapi import APIRouter, Depends

from app.core.db.dependencies import get_db

from app.modules.brands.schemas import (
    BrandCreate,
    BrandUpdate,
)

from app.modules.auth.current_workspace import (
    get_current_workspace,
)

from app.modules.brands.service import (
    create_brand,
    get_brand,
    get_brands,
    update_brand,
    delete_brand,
)

router = APIRouter(
    prefix="/brands",
    tags=["Brands"]
)


@router.post("/")
async def create_brand_route(
    payload: BrandCreate,
    session=Depends(get_db),
    workspace_id=Depends(get_current_workspace),
):
    brand_id = await create_brand(
        session=session,
        workspace_id=workspace_id,
        payload=payload,
    )

    return {
        "brand_id": str(brand_id)
    }


@router.get("/")
async def get_all_brands(
    session=Depends(get_db),
    workspace_id=Depends(get_current_workspace),
):
    return await get_brands(
        session=session,
        workspace_id=workspace_id,
    )


@router.get("/{brand_id}")
async def get_single_brand(
    brand_id: str,
    session=Depends(get_db),
    workspace_id=Depends(get_current_workspace),
):
    return await get_brand(
        session=session,
        workspace_id=workspace_id,
        brand_id=brand_id,
    )


@router.put("/{brand_id}")
async def update_brand_route(
    brand_id: str,
    payload: BrandUpdate,
    session=Depends(get_db),
    workspace_id=Depends(get_current_workspace),
):
    return await update_brand(
        session=session,
        workspace_id=workspace_id,
        brand_id=brand_id,
        payload=payload,
    )


@router.delete("/{brand_id}")
async def delete_brand_route(
    brand_id: str,
    session=Depends(get_db),
    workspace_id=Depends(get_current_workspace),
):
    return await delete_brand(
        session=session,
        workspace_id=workspace_id,
        brand_id=brand_id,
    )
# from fastapi import APIRouter, Depends

# from app.core.db.dependencies import get_db

# from app.modules.brands.schemas import BrandCreate,BrandUpdate


# from app.modules.auth.current_workspace import (
#     get_current_workspace
# )
# from app.modules.brands.service import (
#     create_brand,
#     get_brand,
#     get_brands,
#     update_brand,
#     delete_brand,   
# )

# router = APIRouter(
#     prefix="/brands",
#     tags=["Brands"]
# )


# @router.post("/")
# async def create_brand_route(
#     payload: BrandCreate,
#     session=Depends(get_db),
#     workspace_id=Depends(get_current_workspace)
# ):
#     brand_id = await create_brand(
#         session=session,
#         workspace_id=workspace_id,
#         payload=payload,
#     )

#     return {
#         "brand_id": str(brand_id)
#     }


# @router.get("/")
# async def get_all_brands(
#     session=Depends(get_db),
#     workspace_id=Depends(get_current_workspace)
# ):
#     return await get_brands(
#         session=session,
#         workspace_id=workspace_id,
#     )

# @router.get("/{brand_id}")
# async def get_single_brand(
#     brand_id: str,
#     session=Depends(get_db),
# ):
#     return await get_brand(
#         session=session,
#         brand_id=brand_id,
#     )

# @router.put("/{brand_id}")
# async def update_brand_route(
#     brand_id: str,
#     payload: BrandUpdate,
#     session=Depends(get_db),
# ):
#     return await update_brand(
#         session=session,
#         brand_id=brand_id,
#         payload=payload,
#     )


# @router.delete("/{brand_id}")
# async def delete_brand_route(
#     brand_id: str,
#     session=Depends(get_db),
# ):
#     return await delete_brand(
#         session=session,
#         brand_id=brand_id,
#     )