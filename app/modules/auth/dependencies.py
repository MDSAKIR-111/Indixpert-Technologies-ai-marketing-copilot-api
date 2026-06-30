from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.modules.auth.jwt import verify_access_token

security = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):

    try:

        token = credentials.credentials

        payload = verify_access_token(token)

        return {
            "user_id": payload["sub"],
            "workspace_id": payload["workspace_id"],
            "email": payload["email"],
            "role": payload["role"],
        }

    except Exception:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )


# from fastapi import Depends
# from app.core.db.dependencies import get_db


# async def get_current_user(
#     session=Depends(get_db),
# ):
#     return {
#         "user_id": None,
#         "workspace_id": None,
#         "email": None,
#         "role": "owner",
#     }