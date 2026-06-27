import json
import logging

from app.capability.ai_gateway.gemini import generate_content
from app.capability.ai_gateway.strategy_prompt_builder import (
    build_strategy_prompt
)

from app.modules.content_generation.context_service import ContextService

from app.core.db.base_service import SPService

logger = logging.getLogger(__name__)


class ContentStrategyAIService:

    @staticmethod
    async def generate(session, payload):

        logger.info("========== AI CONTENT STRATEGY ==========")

        # --------------------------------------------
        # Step 1 : Load Brand Context
        # --------------------------------------------
        context = await ContextService.get_brand_context(
            session=session,
            brand_id=payload.brand_id,
        )

        logger.info("Brand context loaded successfully.")

        # --------------------------------------------
        # Step 2 : Build Prompt
        # --------------------------------------------
        final_prompt = build_strategy_prompt(context)

        logger.info("Strategy prompt built successfully.")

        # --------------------------------------------
        # Step 3 : Generate Strategy using Gemini
        # --------------------------------------------
        ai_response = await generate_content(final_prompt)

        logger.info("Gemini generated strategy successfully.")

        # --------------------------------------------
        # Step 4 : Convert JSON String to Dictionary
        # --------------------------------------------
        strategy = json.loads(ai_response)

        logger.info("Strategy JSON parsed successfully.")

        # --------------------------------------------
        # Step 5 : Save Strategy
        # --------------------------------------------
        strategy_id = await SPService.write(
            session=session,
            procedure_name="sp_create_content_strategy",
            params={
                "p_brand_id": payload.brand_id,
                "p_strategy_name": strategy["strategy_name"],
                "p_goal": strategy["goal"],
                "p_content_pillars": strategy["content_pillars"],
                "p_posting_frequency": strategy["posting_frequency"],
                "p_platforms": strategy["platforms"],
            },
        )

        logger.info(f"Strategy saved successfully. ID={strategy_id}")

        # --------------------------------------------
        # Step 6 : Return Response
        # --------------------------------------------
        return {
            "strategy_id": strategy_id,
            "strategy": strategy,
        }