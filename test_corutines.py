import asyncio

import pytest_asyncio
import pytest
from loguru import logger

from task import (
    processing_users_data,
    delayed_message,
    adding_number
)

class TestingCorutines:
    @pytest_asyncio.fixture
    async def test_users_data(self):
        return {
            'username': 'Shurik'
        }

    @pytest_asyncio.fixture
    async def test_data(self):
        return {
         'message': 'Привет, асинхронность!',
         'delay': 0.1
      }

    @pytest_asyncio.fixture
    async def test_value_numbers(self):
        return {
        'number1': 23.343,
        'number2': 234
    }

    @pytest.mark.asyncio
    async def test_processing_name(self, test_users_data):
        result = await processing_users_data(test_users_data['username'])
        assert result == {
        'username': 'Shur'
    }
        logger.info('Первый тест прошел успешно!')

    @pytest.mark.asyncio
    async def test_adding_numbers(self, test_value_numbers):
        result = await adding_number(
        test_value_numbers['number1'],
        test_value_numbers['number2']
        )
        assert result == 257.0
        logger.info('Второй тест прошел успешно!')

    @pytest.mark.asyncio
    async def test_delayed_message(self, test_data):
        result = await delayed_message(
            test_data['message'],
            test_data['delay']
        )
        assert result == test_data['message']
        logger.info('Третий тест прошел успешно!')
