#!/usr/bin/env python3
"""
Asyncronous code
"""
import random
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Import wait_random from the previous python file that have been
        written and write an async routine called wait_n that takes in
        2 int arguments n and max_delay.
        wait_random will be spawned  n times with the specified max_delay.

    Args:
        n (int): _description_
        max_delay (int): _description_

    Returns:
        List[float]: _description_
    """
    res = await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
    return sorted(res)
