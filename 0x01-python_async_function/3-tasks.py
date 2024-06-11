#!/usr/bin/env python3
"""Asyncio Task Module"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Method that takes a maximum delay as argument and returns an async task.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: A task that waits for a delay.
    """

    # Create a task that waits for a random delay between 0 and max_delay.
    # The task is returned to be executed later.
    return asyncio.create_task(wait_random(max_delay))
