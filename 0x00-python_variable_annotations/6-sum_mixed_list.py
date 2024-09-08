#!/usr/bin/env python3
""" Type annotation
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Type annotation

    Args:
        mdx_list (List[int, float]):

    Returns:
        float:
    """
    return float(sum(mxd_lst))
