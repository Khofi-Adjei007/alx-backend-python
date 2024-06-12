#!/usr/bin/env python3

"""Module: Learning async programming with generators"""


import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of executing async_comprehension
    four times in parallel.

    This function uses asyncio.gather to run four instances of
    async_comprehension concurrently 
    and measures the total time taken to complete all four.

    Args:
        None

    Returns:
        float: The total runtime in seconds.
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.time()

    return end - start
