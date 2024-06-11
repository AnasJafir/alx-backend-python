#!/usr/bin/env python3
"""
wait_random Module
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously wait for a random amount of time between zero and max_delay.

    Parameters:
    - max_delay: float (optional)
        The maximum delay in seconds.
        Default is 10.

    Returns:
    - float
        The delay in seconds.

    """

    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
