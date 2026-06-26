from app.core.db.base_service import SPService


class ContentCalendarService:

    @staticmethod
    async def create(session, payload):

        return await SPService.write(
            session=session,
            procedure_name="sp_create_content_calendar",
            params={
                "p_brand_id": payload.brand_id,
                "p_title": payload.title,
                "p_content_type": payload.content_type,
                "p_platform": payload.platform,
                "p_scheduled_date": payload.scheduled_date,
            },
        )

    @staticmethod
    async def get(session, calendar_id):

        return await SPService.one(
            session=session,
            procedure_name="sp_get_content_calendar",
            params={
                "p_id": calendar_id
            },
        )

    @staticmethod
    async def list(session):

        return await SPService.many(
            session=session,
            procedure_name="sp_list_content_calendar"
        )

    @staticmethod
    async def update(session, calendar_id, payload):

        return await SPService.write(
            session=session,
            procedure_name="sp_update_content_calendar",
            params={
                "p_id": calendar_id,
                "p_title": payload.title,
                "p_content_type": payload.content_type,
                "p_platform": payload.platform,
                "p_scheduled_date": payload.scheduled_date,
                "p_status": payload.status,
            },
        )

    @staticmethod
    async def delete(session, calendar_id):

        return await SPService.write(
            session=session,
            procedure_name="sp_delete_content_calendar",
            params={
                "p_id": calendar_id
            },
        )