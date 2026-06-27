from app.core.db.base_service import SPService
from app.modules.social_publish.service import SocialPublishService


class PublisherService:

    @staticmethod
    async def publish(session, calendar_id):

        calendar = await SPService.one(
            session=session,
            procedure_name="sp_get_content_calendar",
            params={
                "p_id": calendar_id
            }
        )

        if not calendar:
            raise Exception("Calendar not found.")

        generated_content = await SPService.one(
            session=session,
            procedure_name="sp_get_generated_content",
            params={
                "p_id": calendar["generated_content_id"]
            }
        )

        if not generated_content:
            raise Exception("Generated content not found.")

        social_account = await SPService.one(
            session=session,
            procedure_name="sp_get_social_account_by_platform",
            params={
                "p_brand_id": calendar["brand_id"],
                "p_platform": calendar["platform"]
            }
        )

        if not social_account:
            raise Exception(
                f"{calendar['platform']} account not connected."
            )

        return await SocialPublishService.publish(
            platform=calendar["platform"],
            social_account=social_account,
            generated_content=generated_content,
        )