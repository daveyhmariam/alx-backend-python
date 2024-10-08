#!/usr/bin/env python3
""" Type annotation
"""

from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Type annotation

    Args:
        lst (Iterable[Sequence]):

    Returns:
        List[Tuple[Sequence, int]]:
    """
    return [(i, len(i)) for i in lst]
