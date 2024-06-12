#!/usr/bin/env python3

"""Module: Learning async programming generators"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Generates a sequence of 10 random float
    numbers asynchronously.

    The coroutine will sleep for 1 second between
    generating each number.

    Args:
        None

    Returns:
        Generator[float, None, None]: A generator that yields
        random float numbers between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
