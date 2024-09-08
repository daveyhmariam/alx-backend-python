#!/usr/bin/env python3
"""
Asyncronous code
"""
import random
import asyncio
import time


wait_random = __import__('0-basic_async_syntax').wait_random
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure_time function with integers n and max_delay
    as arguments that measures the total execution time for
    wait_n(n, max_delay), and returns total_time / n.

    Args:
        n (int): Total spawned
        max_delay (int): max delay

    Returns:
        float: Time elapsed average
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    return float((end - start) / n)
