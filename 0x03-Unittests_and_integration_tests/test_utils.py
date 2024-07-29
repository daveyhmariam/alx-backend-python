#!/usr/bin/env python3


import utils
import unittest
from parameterized import parameterized
from typing import Dict, Tuple, Union


class TestAccessNestedMap(unittest.TestCase):
    """Tests the `access_nested_map` function."""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self,
                               nested_map: Dict[str, Union[int, Dict]],
                               path: Tuple[str, ...],
                               expected: Union[Dict, int]) -> None:
        """Tests `access_nested_map`'s output."""
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self,
                                         nested_map:
                                         Dict[str, Union[int, Dict]],
                                         path: Tuple[str, ...],
                                         exception: Exception) -> None:
        """Tests `access_nested_map`'s exception raising."""
        with self.assertRaises(exception):
            utils.access_nested_map(nested_map, path)
