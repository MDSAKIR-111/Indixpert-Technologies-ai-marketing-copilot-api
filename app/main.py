from fastapi import FastAPI
from sqlalchemy import text
from app.v1.call_all_route import api_router
import asyncio

from app.capability.ai_gateway.gemini import generate_content
from app.core.db.session import engine
from app.core.db.scheduler import start_scheduler, stop_scheduler

app = FastAPI()

app.include_router(api_router)


@app.on_event("startup")
async def on_startup():
    start_scheduler()


@app.on_event("shutdown")
async def on_shutdown():
    stop_scheduler()


@app.get("/db-check")
async def db_check():

    async with engine.connect() as conn:
        result = await conn.execute(
            text("SELECT 1")
        )

    return {
        "database": "connected",
        "result": result.scalar()
    }