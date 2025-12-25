import asyncio
from typing import Dict

async def processing_users_data(name: str) -> Dict[str, str]:
    await asyncio.sleep(1)
    processing_name: str = name.strip().lower().capitalize()

    return {
        'username': processing_name
    }


async def adding_number(number1: int | float, number2: int | float, timer=1) -> int | float:
    await asyncio.sleep(timer)
    return number1 + number2

async def delayed_message(message, delay):
    await asyncio.sleep(delay)
    return message

async def main():
    result = await delayed_message('Привет, асинхронность!', 1)
    result2 = await processing_users_data('shura  ', '83fhuefheuhc', 18)
    print(result2)

