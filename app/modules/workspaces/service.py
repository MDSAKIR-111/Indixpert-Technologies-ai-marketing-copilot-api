from app.core.db.base_service import SPService


async def create_workspace(
    session,
    workspace_name,
    email,
    full_name,
):

    workspace_id = await SPService.run(
        session,
        "create_workspace_with_owner",
        {
            "p_workspace_name": workspace_name,
            "p_email": email,
            "p_full_name": full_name,
        }
    )

    return workspace_id