from app.core.db.base_service import SPService


async def create_workspace(
    session,
    user_id,
    workspace_name,
):

    # Check if current user already has a workspace
    existing = await SPService.one(
        session=session,
        procedure_name="sp_get_workspace",
        params={
            "p_user_id": user_id,
        },
    )

    if existing:
        return {
            "success": False,
            "message": "Workspace already exists.",
            "workspace_id": existing["workspace_id"],
        }

    workspace = await SPService.run(
        session=session,
        procedure_name="sp_create_workspace",
        params={
            "p_user_id": user_id,
            "p_workspace_name": workspace_name,
        },
        fetch_one=True,
    )

    return {
        "success": True,
        "message": "Workspace created successfully.",
        "workspace_id": workspace["workspace_id"],
    }


async def get_workspace(
    session,
    user_id,
):
    return await SPService.one(
        session=session,
        procedure_name="sp_get_workspace",
        params={
            "p_user_id": user_id,
        },
    )