from fastapi import APIRouter, Depends

from app.core.db.dependencies import get_db
from app.modules.auth.schemas import (
    RegisterRequest,
    LoginRequest,
)
from app.modules.auth.service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
async def register(
    payload: RegisterRequest,
    session=Depends(get_db),
):
    return await AuthService.register(
        session=session,
        payload=payload,
    )


@router.post("/login")
async def login(
    payload: LoginRequest,
    session=Depends(get_db),
):
    return await AuthService.login(
        session=session,
        payload=payload,
    )

