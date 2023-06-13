import asyncio
import asyncpg

from time import time
from config import USER, PASSWORD, HOST, PORT, DB_NAME


async def get_async_session():
    dsn = 'postgres://{}:{}@{}:{}/{}'.format(
        USER, PASSWORD, HOST, PORT, DB_NAME
    )
    async with asyncpg.create_pool(dsn) as pool:
        async with pool.acquire() as conn:
            yield conn

async def update_data(session, current_table: str, destination_table: str):
    stmt = '''
    update {1}
    set status = {0}.status
    from {0}
    where {0}.name = left({1}.name, strpos({1}.name, '.') - 1);'''.format(current_table, destination_table)
    start_time = time()
    data = await session.execute(stmt)
    print(data)
    print(f'UPDATE time: {time() - start_time}')

async def start():
    async for session in get_async_session():
        await update_data(
            session,
            current_table='short_names',
            destination_table='full_names'
        )

def main():
    asyncio.run(start())


if __name__ == '__main__':
    main()
