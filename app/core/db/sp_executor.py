from sqlalchemy import text


def build_query(sp_name: str, params: dict):
    placeholders = ", ".join(
        [f":{key}" for key in params.keys()]
    )

    return text(
        f"SELECT * FROM {sp_name}({placeholders})"
    )


async def execute_sp_write(
    session,
    sp_name: str,
    params: dict = None,
):
    params = params or {}

    query = build_query(
        sp_name,
        params
    )

    result = await session.execute(
        query,
        params
    )

    await session.commit()

    return result.scalar()


async def execute_sp_one(
    session,
    sp_name: str,
    params: dict = None,
):
    params = params or {}

    query = build_query(
        sp_name,
        params
    )
    print(query)
    print(params)
    result = await session.execute(
        query,
        params
    )

    row = result.mappings().first()
    print("Row =", row)
    if not row:
        return None

    return dict(row)


async def execute_sp_many(
    session,
    sp_name: str,
    params: dict = None,
):
    params = params or {}

    query = build_query(
        sp_name,
        params
    )

    result = await session.execute(
        query,
        params
    )

    rows = result.mappings().all()

    return [
        dict(row)
        for row in rows
    ]

async def execute_sp(
    session,
    sp_name: str,
    params: dict = None,
    fetch_one: bool = False,
):
    params = params or {}

    placeholders = ", ".join(
        [f":{k}" for k in params.keys()]
    )

    query = text(
        f"SELECT * FROM {sp_name}({placeholders})"
    )

    result = await session.execute(
        query,
        params
    )

    if not fetch_one:
        await session.commit()
        return result.scalar()

    row = result.mappings().first()

    if not row:
        return None

    return dict(row)