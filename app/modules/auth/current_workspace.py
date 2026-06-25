from fastapi import Depends

from app.modules.auth.dependencies import get_current_user


async def get_current_workspace(
    current_user=Depends(get_current_user)
):
    return current_user["workspace_id"]