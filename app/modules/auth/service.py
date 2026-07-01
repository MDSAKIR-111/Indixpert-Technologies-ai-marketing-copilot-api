from app.core.db.base_service import SPService
from app.modules.auth.password import (
    hash_password,
    verify_password,
)
from app.modules.auth.jwt import create_access_token


class AuthService:

    @staticmethod
    async def register(session, payload):

        # Check if user already exists
        existing_user = await SPService.one(
            session=session,
            procedure_name="sp_login_user",
            params={
                "p_email": payload.email,
            },
        )


        if existing_user:
            raise Exception("Email already registered.")

        password_hash = hash_password(payload.password)

        workspace_id = await SPService.write(
            session=session,
            procedure_name="sp_register_user",
            params={
                "p_workspace_name": payload.workspace_name,
                "p_email": payload.email,
                "p_full_name": payload.full_name,
                "p_password_hash": password_hash,
            },
        )

        return {
            "message": "Registration successful.",
            "workspace_id": workspace_id,
        }

    @staticmethod
    async def login(session, payload):

        user = await SPService.one(
            session=session,
            procedure_name="sp_login_user",
            params={
                "p_email": payload.email,
            },
        )

        if not user:
            raise Exception("Invalid email or password.")

        if not verify_password(
            payload.password,
            user["password_hash"],
        ):
            raise Exception("Invalid email or password.")

        token = create_access_token(
            {
                "sub": str(user["user_id"]),
                "workspace_id": str(user["workspace_id"]),
                "email": user["email"],
                "role": user["role"],
            }
        )

        await SPService.run(
            session=session,
            procedure_name="sp_update_last_login",
            params={
                "p_user_id": user["user_id"],
            },
        )

        return {
            "access_token": token,
            "token_type": "bearer",
        }