#!/usr/bin/env python3

""" Async Programming """

import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay and
    returns the list of delays in ascending order.

    Parameters:
        n (int): Number of times to spawn wait_random.
        max_delay (int): The maximum value for the random delay.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    wait_random = __import__('0-basic_async_syntax').wait_random
    delay_list = [wait_random(max_delay) for _ in range(n)]
    completed_tasks = []

    for task in asyncio.as_completed(delay_list):
        completed_tasks.append(await task)

    return completed_tasks
