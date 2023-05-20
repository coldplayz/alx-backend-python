#!/usr/bin/env python3
"""Test module for utils.py.
"""
from unittest import TestCase, mock
from typing import Mapping, Dict, List, Tuple, Sequence, Any, Callable
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(TestCase):
    """Implementation class for testing GithubOrgClient class.
    """
    @parameterized.expand(['google', 'abc'])
    @mock.patch('client.get_json', autospec=True)
    def test_org(self, org, mock_get_json):
        """Test the client.GithubOrgClient.org property.
        """
        # create an instance of GithubOrgClient
        gitClient = GithubOrgClient(org)
        # set return value of the external dependency - get_json
        mock_get_json.return_value = {'test': True}
        # fetch the property (which calls get_json)
        res = gitClient.org
        # test
        self.assertIsInstance(res, dict)
        mock_get_json.assert_called_once_with(
                gitClient.ORG_URL.format(org=org),
                )

    def test_public_repos_url(self):
        """Test the client.GithubOrgClient._public_repos_url property.
        """
        # use patch as a context manager to mock org
        with mock.patch(
                'client.GithubOrgClient.org',
                new_callable=mock.PropertyMock,
                ) as mock_org:
            # org should be a dict with the repos_url key;
            # ..._public_repos_url will want to get it.
            mock_org.return_value = {'repos_url': "https://greenbel.tech"}
            # create class instance
            gitClient = GithubOrgClient('google')
            res = gitClient._public_repos_url
            # test
            self.assertEqual(res, "https://greenbel.tech")
