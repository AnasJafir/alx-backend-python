#!/usr/bin/env python3
"""Runtime Module"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the execution time of wait_n function
    and returns the average time per coroutine execution.

    Parameters:
    - n: int
        The number of times to repeat the wait_n function.
    - max_delay: int
        The maximum delay in seconds.

    Returns:
    - float
        The average time per coroutine execution in seconds.
    """
    # Record the start time
    start_time = time.time()

    # Call wait_n function num_iterations times
    asyncio.run(wait_n(n, max_delay))

    # Record the end time
    end_time = time.time()

    # Calculate the average time per iteration
    total_time = (end_time - start_time) / n

    # Return the average time per iteration
    return total_time
