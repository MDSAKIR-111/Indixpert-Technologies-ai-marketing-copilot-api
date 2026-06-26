from app.capability.ai_gateway.prompt_builder import build_prompt
from app.capability.ai_gateway.gemini import generate_content

from app.modules.content_generation.context_service import ContextService

from app.core.db.base_service import SPService

import logging

logger = logging.getLogger(__name__)


class ContentGenerationAIService:

    @staticmethod
    async def generate(session, payload):

        logger.info("========== AI CONTENT GENERATION ==========")

        # -------------------------------------------------
        # Load Complete Brand Context
        # -------------------------------------------------

        context = await ContextService.get_brand_context(
            session,
            payload.brand_id
        )

        logger.info("Brand context loaded successfully.")

        # -------------------------------------------------
        # Build Prompt
        # -------------------------------------------------

        final_prompt = build_prompt(
            context=context,
            user_prompt=f"""
            Platform: {payload.platform}

            Content Type: {payload.content_type}

            Request:
            {payload.prompt}
            """
        )

        logger.info("========== FINAL PROMPT ==========")
        logger.info(final_prompt)
        logger.info("==================================")
        # -------------------------------------------------
        # Gemini
        # -------------------------------------------------

        ai_response = await generate_content(final_prompt)

        logger.info("Gemini response generated.")

        # -------------------------------------------------
        # Save Generated Content
        # -------------------------------------------------

        content_id = await SPService.write(
            session=session,
            procedure_name="sp_create_generated_content",
            params={
                "p_brand_id": payload.brand_id,
                "p_content_type": payload.content_type,
                "p_prompt": payload.prompt,
                "p_generated_text": ai_response,
                "p_platform": payload.platform,
            }
        )

        logger.info(f"Generated content saved. ID={content_id}")

        return {
            "content_id": content_id,
            "generated_text": ai_response
        }

    @staticmethod
    async def edit(
        session,
        content_id,
        instruction,
    ):

        try:

            logger.info("========== AI CONTENT EDIT ==========")

            # -------------------------------------------------
            # Load Existing Content
            # -------------------------------------------------

            content = await SPService.one(
                session=session,
                procedure_name="sp_get_generated_content",
                params={
                    "p_id": content_id
                }
            )

            if not content:
                raise Exception("Content not found.")

            logger.info("Existing content loaded.")

            # -------------------------------------------------
            # Load Full Brand Context
            # -------------------------------------------------

            context = await ContextService.get_brand_context(
                session,
                content["brand_id"]
            )

            logger.info("Brand context loaded.")

            # -------------------------------------------------
            # Build Edit Prompt
            # -------------------------------------------------

            final_prompt = f"""
            {build_prompt(context=context, user_prompt="")}

            ==================================================
            EXISTING CONTENT
            ==================================================

            {content["generated_text"]}

            ==================================================
            EDIT REQUEST
            ==================================================

            {instruction}

            ==================================================
            EDIT RULES
            ==================================================

            Preserve:
            - Brand voice
            - Marketing goal
            - Target audience
            - Company products
            - Platform suitability

            Only apply the requested changes.

            Do not rewrite unrelated sections.

            Return ONLY the final updated content.
            """

            logger.info("Prompt built successfully.")

            # -------------------------------------------------
            # Gemini
            # -------------------------------------------------

            ai_response = await generate_content(final_prompt)

            logger.info("Gemini completed content editing.")

            # -------------------------------------------------
            # Update Content
            # -------------------------------------------------

            await SPService.write(
                session=session,
                procedure_name="sp_update_generated_content",
                params={
                    "p_content_id": content_id,
                    "p_generated_text": ai_response,
                }
            )

            logger.info("Generated content updated.")

            # -------------------------------------------------
            # Get Version Count
            # -------------------------------------------------

            versions = await SPService.many(
                session=session,
                procedure_name="sp_get_generated_content_versions",
                params={
                    "p_generated_content_id": content_id
                }
            )

            next_version = len(versions) + 1

            logger.info(f"Creating Version {next_version}")

            # -------------------------------------------------
            # Save Version
            # -------------------------------------------------

            await SPService.write(
                session=session,
                procedure_name="sp_create_generated_content_version",
                params={
                    "p_generated_content_id": content_id,
                    "p_version_number": next_version,
                    "p_generated_text": ai_response,
                }
            )

            logger.info("Version saved.")

            logger.info("========== AI EDIT COMPLETED ==========")

            return {
                "message": "Content edited successfully.",
                "content_id": content_id,
                "version": next_version,
                "generated_text": ai_response,
            }

        except Exception as e:

            logger.exception("AI Edit Failed")

            raise e