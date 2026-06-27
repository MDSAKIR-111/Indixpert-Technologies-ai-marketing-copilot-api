from fastapi import Depends
from app.core.db.dependencies import get_db


async def get_current_user(
    session=Depends(get_db),
):
    return {
        "user_id": None,
        "workspace_id": None,
        "email": None,
        "role": "owner",
    }