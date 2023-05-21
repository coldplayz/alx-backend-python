#!/usr/bin/env python3
"""Test module for utils.py.
"""
from unittest import TestCase, mock
from typing import Mapping, Dict, List, Tuple, Sequence, Any, Callable
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD
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

    @mock.patch('client.get_json', autospec=True)
    def test_public_repos(self, mock_get_json):
        """Test the client.GithubOrgClient.public_repos method.
        """
        mock_get_json.return_value = [
                {'name': 'repo1'},
                {'name': 'repo2'},
                {'name': 'repo3'},
                {'name': 'repo4'},
                {'name': 'repo5'},
                ]
        with mock.patch(
                'client.GithubOrgClient._public_repos_url',
                new_callable=mock.PropertyMock,
                ) as mock_pru:
            mock_pru.return_value = 'https://greenbel.tech'
            # create class instance
            gitClient = GithubOrgClient('abc')
            res = gitClient.public_repos()
            # test
            expected = ['repo1', 'repo2', 'repo3', 'repo4', 'repo5']
            self.assertEqual(res, expected)
            mock_get_json.assert_called_once_with("https://greenbel.tech")
            mock_pru.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ])
    def test_has_license(self, repo, licence_key, expected):
        """Test the client.GithubOrgClient.has_license static method.
        """
        gitClient = GithubOrgClient('abc')
        self.assertEqual(gitClient.has_license(repo, licence_key), expected)


@parameterized_class(
        ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
        TEST_PAYLOAD,
        )
class TestIntegrationGithubOrgClient(TestCase):
    """Integration tests for client.GithubOrgClient.
    """
    @classmethod
    def setUpClass(cls):
        """Setup called once per class, and for each test method therein.
        """
        # create patcher for requests.get()
        cls.get_patcher = mock.patch('utils.requests', autospec=True)
        # retrieve the mocked method
        mock_get = cls.get_patcher.start()  # attach to instance
        # create instance
        # prepare json mock
        # json = mock.Mock()
        # json.side_effect = [cls.org_payload, cls.repos_payload]
        # attach json mock to return of get (as the response object)
        # mock_get.return_value = json
        # attach to each TestCase instance for each test method
        cls.mock_get = mock_get

    @classmethod
    def tearDownClass(cls):
        """Stop the patcher.
        """
        cls.get_patcher.stop()

    def test_public_repos_integration(self):
        """Implement the integration test.
        """
        # prepare response mock as return of requests.get
        response_mock = mock.Mock()
        # self. should eventually lookup cls.
        response_mock.json.side_effect = [
                self.org_payload,
                self.repos_payload,
                ]
        # attach response mock to return of get (as the response object)
        self.mock_get.return_value = response_mock

        # test
        gitClient = GithubOrgClient('abc')
        res = gitClient.public_repos()
        self.assertEqual(res, self.expected_repos)
