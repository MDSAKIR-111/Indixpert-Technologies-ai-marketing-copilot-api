from app.core.db.base_service import SPService


class ContextService:

    @staticmethod
    async def get_brand_context(session, brand_id):

        # Brand
        brand = await SPService.one(
            session=session,
            procedure_name="sp_get_brand",
            params={
                "p_brand_id": brand_id
            }
        )

        # Brand Knowledge
        knowledge = await SPService.one(
            session=session,
            procedure_name="sp_get_brand_context",
            params={
                "p_brand_id": brand_id
            }
        )

        # Content Strategy
        strategy = await SPService.one(
            session=session,
            procedure_name="sp_get_content_strategy",
            params={
                "p_brand_id": brand_id
            }
        )

        return {
            "brand": brand or {},
            "knowledge": knowledge or {},
            "strategy": strategy or {},
        }