from app.core.db.base_service import SPService


class DashboardService:

    @staticmethod
    async def overview(session, workspace_id):

        return await SPService.one(
            session=session,
            procedure_name="sp_get_dashboard_overview",
            params={
                "p_workspace_id": workspace_id
            }
        )

    @staticmethod
    async def recent_activity(session, workspace_id):

        return await SPService.many(
            session=session,
            procedure_name="sp_get_recent_activity",
            params={
                "p_workspace_id": workspace_id
            }
        )