from app.core.db.base_service import SPService
from app.modules.social_publish.service import SocialPublishService
from fastapi import HTTPException
from datetime import datetime, timezone


class PublisherService:

    @staticmethod
    async def publish(session, workspace_id, calendar_id):

        calendar = await SPService.one(
            session=session,
            procedure_name="sp_get_content_calendar",
            params={
                "p_workspace_id": workspace_id,
                "p_id": calendar_id
            }
        )

        if not calendar:
            raise HTTPException(status_code=404, detail="Calendar not found.")

        generated_content = await SPService.one(
            session=session,
            procedure_name="sp_get_generated_content",
            params={"p_id": calendar["generated_content_id"]}
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
            raise Exception(f"{calendar['platform']} account not connected.")

        try:
            result = await SocialPublishService.publish(
                platform=calendar["platform"],
                social_account=social_account,
                generated_content=generated_content,
            )

            await SPService.write(
                session=session,
                procedure_name="sp_create_publish_log",
                params={
                    "p_workspace_id": workspace_id,
                    "p_brand_id": calendar["brand_id"],
                    "p_generated_content_id": calendar["generated_content_id"],
                    "p_content_calendar_id": calendar_id,
                    "p_social_account_id": social_account["id"],
                    "p_platform": calendar["platform"],
                    "p_post_id": result.get("post_id") if isinstance(result, dict) else None,
                    "p_status": "success",
                    "p_retry_count": 0,
                    "p_error_message": None,
                    "p_published_at": datetime.now(timezone.utc),
                }
            )

            return result

        except Exception as e:
            await SPService.write(
                session=session,
                procedure_name="sp_create_publish_log",
                params={
                    "p_workspace_id": workspace_id,
                    "p_brand_id": calendar["brand_id"],
                    "p_generated_content_id": calendar["generated_content_id"],
                    "p_content_calendar_id": calendar_id,
                    "p_social_account_id": social_account["id"],
                    "p_platform": calendar["platform"],
                    "p_post_id": None,
                    "p_status": "failed",
                    "p_retry_count": 0,
                    "p_error_message": str(e),
                    "p_published_at": None,
                }
            )
            raise

    @staticmethod
    async def get_logs(session, workspace_id):
        return await SPService.many(
            session=session,
            procedure_name="sp_list_publish_logs",
            params={"p_workspace_id": workspace_id}
        )