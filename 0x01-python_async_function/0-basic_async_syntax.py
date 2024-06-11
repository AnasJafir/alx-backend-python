#!/usr/bin/env python3
"""
wait_random Module
"""
import asyncio
import random


async def wait_random(max_delay=10):
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

    delay = random.uniform(0, float(max_delay))
    await asyncio.sleep(delay)
    return delay
