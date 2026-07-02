from app.core.db.base_service import SPService


class ContentCalendarService:

    @staticmethod
    async def create(session, workspace_id, payload):

        content = await SPService.one(
            session=session,
            procedure_name="sp_get_generated_content",
            params={
                "p_id": payload.generated_content_id
            }
        )

        if not content:
            raise Exception("Generated content not found.")

        return await SPService.write(
            session=session,
            procedure_name="sp_create_content_calendar",
            params={
                "p_generated_content_id": payload.generated_content_id,
                "p_brand_id": content["brand_id"],
                "p_title": content["content_type"],
                "p_content_type": content["content_type"],
                "p_platform": content["platform"],
                "p_scheduled_datetime": payload.scheduled_datetime.replace(tzinfo=None),
            },
        )

    @staticmethod
    async def get(session, workspace_id, calendar_id):

        return await SPService.one(
            session=session,
            procedure_name="sp_get_content_calendar",
            params={
                "p_workspace_id": workspace_id,
                "p_id": calendar_id
            },
        )

    @staticmethod
    async def list(session, workspace_id):

        return await SPService.many(
            session=session,
            procedure_name="sp_list_content_calendar",
            params={
                "p_workspace_id": workspace_id
            }
        )

    @staticmethod
    async def update(session, workspace_id, calendar_id, payload):

        calendar = await SPService.one(
            session=session,
            procedure_name="sp_get_content_calendar",
            params={
                "p_workspace_id": workspace_id,   # 👈 fix: pehle missing tha
                "p_id": calendar_id
            }
        )

        if not calendar:
            raise Exception("Calendar entry not found.")

        return await SPService.write(
            session=session,
            procedure_name="sp_update_content_calendar",
            params={
                "p_workspace_id": workspace_id,
                "p_id": calendar_id,
                "p_title": calendar["title"],
                "p_content_type": calendar["content_type"],
                "p_platform": calendar["platform"],
                "p_scheduled_datetime": payload.scheduled_datetime.replace(tzinfo=None),
                "p_status": payload.status,
            },
        )

    @staticmethod
    async def delete(session, workspace_id, calendar_id):

        return await SPService.write(
            session=session,
            procedure_name="sp_delete_content_calendar",
            params={
                "p_workspace_id": workspace_id,   # 👈 fix: pehle missing tha
                "p_id": calendar_id
            },
        )