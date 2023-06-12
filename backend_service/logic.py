from typing import Coroutine

from fastapi import HTTPException


class AioRedis:
    def __init__(self, connection):
        self.connection = connection

    async def find_data(self, phone: str) -> Coroutine:
        """
        :param phone: gets existed in cache phone number
        :return: Coroutine
        """
        address = await self.connection.get(phone)
        if address:
            return {
                'address': address
            }
        else:
            raise HTTPException(status_code=404, detail='This phone dose not exist')

    async def add_data(self, phone: str, address: str) -> Coroutine:
        """
        :param phone: gets not existed in cache phone number
        :param address: gets any address str
        :return: Coroutine
        """
        cache = await self.connection.set(phone, address, nx=True)
        if cache:
            return {
                'phone': phone,
                'address': address
            }
        else:
            raise HTTPException(status_code=409, detail='data already exists')

    async def update_data(self, phone: str, address: str) -> Coroutine:
        """
        :param phone: gets existed in cache phone number
        :param address: gets any address str
        :return:
        """
        if await self.connection.get(phone):
            await self.connection.set(phone, address, xx=True)
            return {
                'phone': phone,
                'new_address': address
            }
        else:
            raise HTTPException(status_code=404, detail='This phone dose not exist')