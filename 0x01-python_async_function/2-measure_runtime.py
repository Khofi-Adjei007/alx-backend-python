#!/usr/bin/env python3

"""Hehe"""

import time
import asyncio


def measure_time(n: int, max_delay: int) -> float:

    """
    Method: measure_time - measures total execution time
    Parameters:
        n - runs wait_random n number of times
        max_delay- specifies the max delay
    Return: total time over runs

    """

    wait_n = __import__('1-concurrent_coroutines').wait_n

    starttime = time.time()
    asyncio.run(wait_n(n, max_delay))
    endtime = time.time()

    return (endtime - starttime) / n
