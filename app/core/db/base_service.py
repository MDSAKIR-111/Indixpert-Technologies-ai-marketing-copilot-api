from app.core.db.sp_executor import (
    execute_sp_write,
    execute_sp_one,
    execute_sp_many,
    execute_sp
)


class SPService:

    @staticmethod
    async def write(
        session,
        procedure_name,
        params=None,
    ):
        return await execute_sp_write(
            session=session,
            sp_name=procedure_name,
            params=params,
        )

    @staticmethod
    async def one(
        session,
        procedure_name,
        params=None,
    ):
        return await execute_sp_one(
            session=session,
            sp_name=procedure_name,
            params=params,
        )

    @staticmethod
    async def many(
        session,
        procedure_name,
        params=None,
    ):
        return await execute_sp_many(
            session=session,
            sp_name=procedure_name,
            params=params,
        )

    @staticmethod
    async def run(
        session,
        procedure_name: str,
        params: dict = None,
        fetch_one: bool = False,
    ):
        return await execute_sp(
            session=session,
            sp_name=procedure_name,
            params=params,
            fetch_one=fetch_one,
        )