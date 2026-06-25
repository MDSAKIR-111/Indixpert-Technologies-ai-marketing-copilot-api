from app.core.db.base_service import SPService


async def create_brand_knowledge(
    session,
    payload,
):
    return await SPService.run(
        session=session,
        procedure_name="sp_create_brand_knowledge",
        params={
            "p_brand_id": payload.brand_id,
            "p_company_description": payload.company_description,
            "p_target_audience": payload.target_audience,
            "p_products_services": payload.products_services,
            "p_brand_voice": payload.brand_voice,
            "p_competitors": payload.competitors,
            "p_ai_instructions": payload.ai_instructions,
        }
    )