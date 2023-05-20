#!/usr/bin/env python3
"""Test module for utils.py.
"""
from unittest import TestCase, mock
from parameterized import parameterized
from utils import access_nested_map, get_json, requests
from typing import Mapping, Dict, List, Tuple, Sequence, Any, Callable

INPUTS: List[Tuple] = [
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ]


class TestAccessNestedMap(TestCase):
    """Implementation class for testing utils.access_nested_map function.
    """
    @parameterized.expand(INPUTS)
    def test_access_nested_map(
            self, nested_map: Mapping, path: Sequence, expected: Any) -> None:
        """Test the function's return."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
        ])
    def test_access_nested_map_exception(
            self, nested_map: Mapping, path: Sequence) -> None:
        """Test exception is raised when invalid map.
        """
        self.assertRaises(KeyError, access_nested_map, nested_map, path)


class TestGetJson(TestCase):
    """Implementation class for testing utils.get_json function.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
        ])
    @mock.patch('utils.requests', autospec=True)
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict,
            mock_requests: mock.Mock
            ) -> None:
        """Test the return of utils.get_json.
        """
        # prepare other needed mocks
        response_mock = mock.Mock()
        response_mock.json.return_value = test_payload
        mock_requests.get.return_value = response_mock

        # use the mocked object in the call to get_json
        payload = get_json(test_url)

        # test usage
        mock_requests.get.assert_called_once_with(test_url)
        self.assertEqual(payload, test_payload)
