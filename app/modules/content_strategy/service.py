from app.core.db.base_service import SPService


async def create_content_strategy(
    session,
    workspace_id,
    payload,
):
    # Verify brand belongs to current workspace
    brand = await SPService.one(
        session=session,
        procedure_name="sp_get_brand",
        params={
            "p_brand_id": payload.brand_id,
        },
    )

    if not brand:
        raise Exception("Brand not found.")

    if str(brand["workspace_id"]) != str(workspace_id):
        raise Exception("Unauthorized.")

    return await SPService.write(
        session=session,
        procedure_name="sp_create_content_strategy",
        params={
            "p_brand_id": payload.brand_id,
            "p_strategy_name": payload.strategy_name,
            "p_goal": payload.goal,
            "p_content_pillars": payload.content_pillars,
            "p_posting_frequency": payload.posting_frequency,
            "p_platforms": payload.platforms,
        },
    )


async def get_strategy(
    session,
    workspace_id,
    brand_id,
):
    # Verify brand belongs to current workspace
    brand = await SPService.one(
        session=session,
        procedure_name="sp_get_brand",
        params={
            "p_brand_id": brand_id,
        },
    )

    if not brand:
        raise Exception("Brand not found.")

    if str(brand["workspace_id"]) != str(workspace_id):
        raise Exception("Unauthorized.")

    return await SPService.one(
        session=session,
        procedure_name="sp_get_content_strategy",
        params={
            "p_brand_id": brand_id,
        },
    )
    
# from app.core.db.base_service import SPService


# async def create_content_strategy(
#     session,
   
#     payload,

# ):
#     return await SPService.write(
#         session=session,
#         procedure_name="sp_create_content_strategy",
#         params={
#             "p_brand_id": payload.brand_id,
#             "p_strategy_name": payload.strategy_name,
#             "p_goal": payload.goal,
#             "p_content_pillars": payload.content_pillars,
#             "p_posting_frequency": payload.posting_frequency,
#             "p_platforms": payload.platforms,
#         }
#     )


# async def get_strategy(
#     session,
#     workspace_id,
#     brand_id,
# ):
#     return await SPService.one(
#         session=session,
#         procedure_name="sp_get_content_strategy",
#         params={
#             "p_brand_id": brand_id,
#         }
#     )