#!/usr/bin/env python3
"""Asyncio Task Module"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously waits for n random delays between 0 and max_delay.

    Args:
        n (int): The number of delays to wait.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: A list of delays sorted in ascending order.
    """
    lst: List[float] = []
    for _ in range(n):
        # Wait for a random delay between 0 and max_delay
        delay: float = await task_wait_random(max_delay)
        lst.append(delay)

    # Sort the list of delays in ascending order
    return sorted(lst)
