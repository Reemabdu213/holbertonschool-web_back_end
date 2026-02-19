#!/usr/bin/env python3
"""Module that contains an async generator coroutine"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yields random numbers between 0 and 10, ten times with 1s delay"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
