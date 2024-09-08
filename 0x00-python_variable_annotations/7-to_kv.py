#!/usr/bin/env python3
""" Type annotation
"""

from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Type annotation

    Args:
        k (str):
        Union (_type_):

    Returns:
        Tuple[str, float]:
    """
    return (k, float(v**2))
