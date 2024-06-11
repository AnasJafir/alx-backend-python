#!/usr/bin/env python3
""" Main file to test async_comprehension. """
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Measure the runtime of async_comprehension 4 times in parallel."""
    start = time.time()
    # asyncio.gather takes the 4 coroutines of async_comprehension
    # and runs them concurently
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.time()
    return end - start
