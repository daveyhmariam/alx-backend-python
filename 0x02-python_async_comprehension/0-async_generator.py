#!/usr/bin/env python3
"""Asyncronous comprehension
"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """async comprehension

    Yields:
        Generator[float, int]:
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
