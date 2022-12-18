import asyncio
from src.classes import Time


async def decrease_time(time_to_wait: Time):
    await asyncio.sleep(time_to_wait)


async def timer(time_to_wait: Time):
    await decrease_time(time_to_wait)
