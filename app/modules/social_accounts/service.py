from app.core.db.base_service import SPService


class SocialAccountService:

    @staticmethod
    async def create(session, workspace_id,payload):

        return await SPService.write(
            session=session,
            procedure_name="sp_create_social_account",
            params={
                "p_workspace_id": workspace_id,
                "p_brand_id": payload.brand_id,
                "p_platform": payload.platform,
                "p_access_token": payload.access_token,
                "p_refresh_token": payload.refresh_token,
                "p_account_id": payload.account_id,
                "p_page_id": payload.page_id,
                "p_expires_at": payload.expires_at,
            },
        )

    @staticmethod
    async def get(session,workspace_id, social_account_id):

        return await SPService.one(
            session=session,
            procedure_name="sp_get_social_account",
            params={
                "p_workspace_id": workspace_id,
                "p_id": social_account_id

            },
        )

    @staticmethod
    async def update(session,workspace_id, social_account_id, payload):

        return await SPService.write(
            session=session,
            procedure_name="sp_update_social_account",
            params={
                "p_workspace_id": workspace_id,
                "p_id": social_account_id,
                "p_platform": payload.platform,
                "p_access_token": payload.access_token,
                "p_refresh_token": payload.refresh_token,
                "p_account_id": payload.account_id,
                "p_page_id": payload.page_id,
                "p_expires_at": payload.expires_at,
            },
        )

    @staticmethod
    async def delete(session,workspace_id,social_account_id):

        return await SPService.write(
            session=session,
            procedure_name="sp_delete_social_account",
            params={
                "p_workspace_id": workspace_id,
                "p_id": social_account_id
            },
        )