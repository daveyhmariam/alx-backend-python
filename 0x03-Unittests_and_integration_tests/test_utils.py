#!/usr/bin/env python3


import utils
import unittest
from parameterized import parameterized
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock


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

    class TestGetJson(unittest.TestCase):
        """Tests the `get_json` function."""
        @parameterized.expand([
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ])
        def test_get_json(self, url: str, payload: Dict):
            att = {"json.return_value": payload}
            with patch("requests.get", return_value=Mock(**att)) as req:
                self.assertEqual(utils.get_json(url), payload)


class TestMemoize(unittest.TestCase):
    """Tests the `memoize` function."""

    def test_memoize(self) -> None:
        """Tests `memoize`'s output."""
        class TestClass:
            def a_method(self):
                return 42

            @utils.memoize
            def a_property(self):
                return self.a_method()
        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
        ) as memo_fxn:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memo_fxn.assert_called_once()
