#!/usr/bin/env python3
"""Test module for utils.py.
"""
from unittest import TestCase, mock
from typing import Mapping, Dict, List, Tuple, Sequence, Any, Callable
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(TestCase):
    """Implementation class for testing client.GithubOrgClient.org property.
    """
    @parameterized.expand(['google', 'abc'])
    @mock.patch('client.get_json', autospec=True)
    def test_org(self, org, mock_get_json):
        """Test that the property fetches the right value.
        """
        # create an instance of GithubOrgClient
        gitClient = GithubOrgClient(org)
        mock_get_json.return_value = {'test': True}
        res = gitClient.org
        # test
        self.assertIsInstance(res, dict)
        mock_get_json.assert_called_once_with(
                gitClient.ORG_URL.format(org=org),
                )
