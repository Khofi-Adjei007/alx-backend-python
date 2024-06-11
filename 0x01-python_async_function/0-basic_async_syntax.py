#!/usr/bin/env python3

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:

    """
    Asynchronous coroutine that waits for a random delay
    between 0 and max_delay seconds (inclusive) and
    returns the delay.

    Args:
        max_delay (int): The maximum value for the random
        delay. Default is 10.

    Returns:
        float: The actual time delayed in seconds.
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
