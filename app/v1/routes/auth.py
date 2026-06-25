from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.get("/health")
async def auth_health():
    return {
        "module": "auth",
        "status": "working"
    }