#!/usr/bin/env python3
""" Type annotation
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Type annotation callable

    Args:
        multiplier (float):
        float (_type_):
    """
    return lambda x: x * multiplier
