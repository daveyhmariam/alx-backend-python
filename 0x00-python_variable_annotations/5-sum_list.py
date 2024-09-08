#!/usr/bin/env python3
""" Type annotation
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Type annotation

    Args:
        input_list (List[float]):

    Returns:
        float: summation
    """
    return float(sum(input_list))
