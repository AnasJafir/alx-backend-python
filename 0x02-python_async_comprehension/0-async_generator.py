#!/usr/bin/env python3
"""
Asynchronous generator that yields random floating point numbers.

This generator will produce 10 random numbers between 0 and 10
with a 1-second delay between each number.
"""
import asyncio
import random
import time
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields random floating point numbers.

    Yields:
        float: A random floating point number between 0 and 10.

    """
    for _ in range(10):
        time.sleep(1)
        yield random.random() * 10
