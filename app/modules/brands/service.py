from app.core.db.base_service import SPService


async def create_brand(
    session,
    workspace_id,
    payload,
):
    return await SPService.write(
        session=session,
        procedure_name="sp_create_brand",
        params={
            "p_workspace_id": workspace_id,
            "p_name": payload.name,
            "p_website": payload.website,
            "p_industry": payload.industry,
        }
    )


async def get_brand(
    session,
    brand_id,
):
    return await SPService.one(
        session=session,
        procedure_name="sp_get_brand",
        params={
            "p_brand_id": brand_id
        }
    )


async def get_brands(
    session,
    workspace_id,
):
    return await SPService.many(
        session=session,
        procedure_name="sp_get_brands",
        params={
            "p_workspace_id": workspace_id
        }
    )


async def update_brand(
    session,
    brand_id,
    payload,
):
    return await SPService.write(
        session=session,
        procedure_name="sp_update_brand",
        params={
            "p_brand_id": brand_id,
            "p_name": payload.name,
            "p_website": payload.website,
            "p_industry": payload.industry,
        }
    )


async def delete_brand(
    session,
    brand_id,
):
    return await SPService.write(
        session=session,
        procedure_name="sp_delete_brand",
        params={
            "p_brand_id": brand_id
        }
    )

