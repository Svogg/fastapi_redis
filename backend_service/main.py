import aioredis as redis
from fastapi import FastAPI

from logic import AioRedis
from shemas import DataSchema

app = FastAPI(
    title='fastapi_redis',
)

session = AioRedis(redis.from_url('redis://redis:6379'))


@app.post('/write_data')
async def write_data(data: DataSchema):
    return await session.add_data(data.phone, data.address)


@app.patch('/write_data')
async def write_data(data: DataSchema):
    return await session.update_data(data.phone, data.address)


@app.get('/check_data')
async def check_data(phone: str):
    return await session.find_data(phone)