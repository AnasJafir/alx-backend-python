#!/usr/bin/env python3
"""Concurrent coroutines module"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """
    Asynchronously waits for n random delays between 0 and max_delay.

    Parameters:
    - n: int
        The number of delays to wait.
    - max_delay: float
        The maximum delay in seconds.

    Returns:
    - list
        A list of delays sorted in ascending order.
    """
    lst = []
    for i in range(n):
        # Wait for a random delay between 0 and max_delay
        delay = await wait_random(max_delay)
        lst.append(delay)

    # Sort the list of delays in ascending order
    return sorted(lst)
