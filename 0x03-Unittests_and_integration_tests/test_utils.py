#!/usr/bin/env python3
"""Test module for utils.py.
"""
from unittest import TestCase
from parameterized import parameterized
from utils import access_nested_map
from typing import Mapping, Dict, List, Tuple, Sequence, Any, Callable

INPUTS: List[Tuple] = [
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ]


class TestAccessNestedMap(TestCase):
    """Implementation class for testing access_nested_map function.
    """
    @parameterized.expand(INPUTS)
    def test_return(self, nested_map: Mapping, path: Sequence, expected: Any) -> None:
        """Test the function's return."""
        self.assertEqual(access_nested_map(nested_map, path), expected)
