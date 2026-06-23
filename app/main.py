from fastapi import FastAPI
from sqlalchemy import text

from app.core.db.session import engine

app = FastAPI()


@app.get("/health")
async def health():
    return {"status": "ok"}


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