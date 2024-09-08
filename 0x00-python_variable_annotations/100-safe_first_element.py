#!/usr/bin/env python3
""" Type annotation
"""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[any]) -> Union[Any, None]:
    """Duck typing

    Args:
        lst (Sequence[any]):

    Returns:
        Union[Any, None]:
    """
    if lst:
        return lst[0]
    else:
        return None
