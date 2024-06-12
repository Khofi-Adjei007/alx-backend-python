#!/usr/bin/env python3

"""Module: Learning async programming generators"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random float numbers generated
    asynchronously.

    This function runs the async_generator 10 times
    and returns a list of the random floats.

    Args:
        None

    Returns:
        List[float]: A list of 10 random float numbers.
    """
    return [i async for i in async_generator()]
