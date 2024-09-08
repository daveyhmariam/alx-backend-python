#!/usr/bin/env python3
""" Type annotation
"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """

    Args:
        lst (Tuple):
        factor (int, optional): Defaults to 2.

    Returns:
        List:
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
