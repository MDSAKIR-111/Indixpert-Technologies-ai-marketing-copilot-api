from app.core.db.base_service import SPService

from app.capability.ai_gateway.gemini import generate_content
class ContentGenerationService:

    @staticmethod
    async def create(session, payload):

        return await SPService.write(
            session=session,
            procedure_name="sp_create_generated_content",
            params={
                "p_brand_id": payload.brand_id,
                "p_content_type": payload.content_type,
                "p_prompt": payload.prompt,
                "p_generated_text": payload.generated_text,
                "p_platform": payload.platform,
            },
        )

    @staticmethod
    async def get(session, content_id):

        return await SPService.one(
            session=session,
            procedure_name="sp_get_generated_content",
            params={
                "p_id": content_id
            },
        )

    @staticmethod
    async def list(session, brand_id):

        return await SPService.many(
            session=session,
            procedure_name="sp_list_generated_content",
            params={
                "p_brand_id": brand_id
            },
        )

    @staticmethod
    async def get_versions(
        session,
        content_id,
    ):
        return await SPService.many(
            session=session,
            procedure_name="sp_get_generated_content_versions",
            params={
                "p_generated_content_id": content_id
            },
        )


    @staticmethod
    async def regenerate(
        session,
        content_id,
        prompt,
    ):
        versions = await SPService.many(
            session=session,
            procedure_name="sp_get_generated_content_versions",
            params={
                "p_generated_content_id": content_id
            },
        )

        next_version = len(versions) + 1

         # Generate AI content
        generated_text = await generate_content(prompt)

        # Write content to the database
        return await SPService.write(
            session=session,
            procedure_name="sp_create_generated_content_version",
            params={
                "p_generated_content_id": content_id,
                "p_version_number": next_version,
                "p_generated_text": generated_text,
            },
        )

    @staticmethod
    async def update(
        session,
        content_id,
        generated_text,
    ):
        return await SPService.write(
            session=session,
            procedure_name="sp_update_generated_content",
            params={
                "p_id": content_id,
                "p_generated_text": generated_text,
            },
        )