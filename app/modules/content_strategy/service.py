from app.core.db.base_service import SPService


async def create_content_strategy(
    session,
    payload,
):
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
        }
    )