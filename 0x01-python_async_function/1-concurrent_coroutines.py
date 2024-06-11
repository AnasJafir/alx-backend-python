#!/usr/bin/env python3
"""Concurrent coroutines module"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously waits for n random delays between 0 and max_delay.

    Parameters:
    - n: int
        The number of delays to wait.
    - max_delay: float
        The maximum delay in seconds.

    Returns:
    - List[float]
        A list of delays sorted in ascending order.
    """
    lst: List[float] = []
    for _ in range(n):
        # Wait for a random delay between 0 and max_delay
        delay: float = await wait_random(max_delay)
        lst.append(delay)

    # Sort the list of delays in ascending order
    return sorted(lst)
