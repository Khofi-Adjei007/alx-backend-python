#!/usr/bin/env python3
"""Module: Learning Async"""

import asyncio
from typing import List


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Runs multiple coroutines concurrently using async/await.

    Args:
        n (int): The number of times to run the coroutine.
        max_delay (int): The maximum delay in seconds inside
        the wait_random coroutine.

    Returns:
        List[float]: A list of the times taken for each task.
    """
    task_wait_random = __import__('3-tasks').task_wait_random
    delay_list = [task_wait_random(max_delay) for _ in range(n)]
    completed_tasks = []

    for task in asyncio.as_completed(delay_list):
        completed_tasks.append(await task)

    return completed_tasks
