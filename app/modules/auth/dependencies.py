from fastapi import Depends

from app.core.db.dependencies import get_db
from app.modules.auth.service import get_user_workspace


async def get_current_user(
    session=Depends(get_db),
):

    email = "jane.doe@example.com"

    user = await get_user_workspace(
        session=session,
        email=email,
    )

    return user