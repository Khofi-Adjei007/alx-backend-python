#!/usr/bin/env python3

"""Module: Await Function"""

import asyncio

def task_wait_random(max_delay: int) -> asyncio.Task:

    """
    Creates and returns an asyncio Task that waits
    for a random delay.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: An asyncio Task that waits for a
        random delay.
    """

    wait_random = __import__('0-basic_async_syntax').wait_random

    return asyncio.create_task(wait_random(max_delay))

