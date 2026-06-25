from sqlalchemy import text


class BaseRepository:

    def __init__(self, session):
        self.session = session

    async def execute_sp(
        self,
        procedure_name: str,
        params: dict | None = None,
    ):
        params = params or {}

        placeholders = ", ".join(
            f":{key}" for key in params.keys()
        )

        query = text(
            f"SELECT * FROM {procedure_name}({placeholders})"
        )

        result = await self.session.execute(
            query,
            params,
        )

        return result.fetchall()